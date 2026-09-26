"""Assess content that the website generated for the simulated user.

Pipeline (paper Sec. 4.5):
  1. Boilerplate removal across captures and prose extraction.
  2. Deterministic measurements (``metrics.analyse_parts``) against the user's
     own inputs (names, objects, reading age) -> tool evidence.
  3. Rubric-based LLM judgement in the persona's frame, G-Eval / Prometheus
     style: explicit criteria with score anchors, evidence before score, per-part
     critique and a concrete change / rewrite for every part.
  4. Batching over images for long outputs, with a synthesis pass.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

from ..llm import LLMClient, LLMError, image_part
from ..personas.schema import Persona
from . import metrics

CRITERIA = {
    "fidelity": "5 = uses all my details (names, relationships, places, objects, events) correctly; 3 = some details missing or changed; 1 = ignores or contradicts what I gave, or invents important people/facts.",
    "coherence": "5 = clear beginning, middle and end, causal flow, consistent characters and pronouns; 3 = mostly follows but with jumps or inconsistencies; 1 = disjointed or contradictory.",
    "age_fit": "5 = vocabulary, sentence length and themes are right for the reading age; 3 = some words/themes too hard or mature; 1 = unsuitable (too difficult, frightening or inappropriate).",
    "language": "5 = no spelling, grammar or formatting errors, no glitches; 3 = a few errors; 1 = many errors, placeholders or broken text.",
    "text_image_fit": "5 = every picture shows what its text says (or complements it); 3 = some pictures unrelated; 1 = pictures contradict the text.",
    "character_consistency": "5 = characters look the same on every page and match my descriptions/photos; 3 = noticeable drift; 1 = characters change identity/appearance.",
    "visual_quality": "5 = attractive, in the style I chose, no artefacts (extra fingers, garbled lettering, distorted faces); 3 = acceptable with flaws; 1 = poor.",
    "emotional_resonance": "5 = feels personal, meaningful and keepsake-worthy to me; 3 = pleasant but generic; 1 = impersonal or upsetting.",
}

JUDGE_TEMPLATE = """You are {name}. You have just used a website that generated something for you. Now examine what it produced, part by part, the way you would - and at the same time be a careful, honest evaluator (do not flatter the website; real users notice mistakes in their own family's names and stories immediately).

=== YOU ===
{profile}

=== WHAT YOU ASKED THE WEBSITE FOR (your own inputs) ===
{inputs}

=== AUTOMATIC MEASUREMENTS (from a text-analysis tool - treat as evidence, but verify against the content) ===
{measurements}

=== THE OUTPUT (captured from the website) ===
{artifact}

=== RUBRIC (score 1-5, give evidence BEFORE the score; use "n/a" when a criterion cannot be judged) ===
{rubric}

{task}"""

PARTS_TASK = """Return ONLY a JSON object:
{
 "artifact_type": "what kind of output this is",
 "parts": [ {"part": "Cover / Title page / Page 1 / ...", "text": "verbatim text of this part as shown (empty if none)", "image_refs": ["I1"], "picture_description": "what the picture actually shows", "reaction": "in character, 1-2 sentences", "problems": [{"criterion": "one of the rubric keys", "evidence": "exact quote or what is visible", "severity": 0-4}], "strengths": ["..."], "suggested_change": "the concrete change you would make to THIS part", "rewrite": "improved text for this part if its text should change, else empty"} ]%s
}
Cover every part of the output in order. Severity: 0 none, 1 cosmetic, 2 minor, 3 major, 4 unacceptable."""

GLOBAL_FIELDS = """,
 "criteria": {"fidelity": {"evidence": "...", "score": 1-5}, "coherence": {...}, "age_fit": {...}, "language": {...}, "text_image_fit": {...}, "character_consistency": {...}, "visual_quality": {...}, "emotional_resonance": {...}},
 "input_fidelity": {"used_correctly": ["..."], "missing": ["..."], "changed": ["..."], "invented": ["..."]},
 "safety_concerns": ["anything unsuitable for a child, or none"],
 "overall_reaction": "in character, 2-4 sentences",
 "keepsake_worthiness": 1-5,
 "would_pay_for_it": "yes / no / maybe + why",
 "top_changes": ["most important change first", "..."]"""

SYNTH_TEMPLATE = """You are {name}. Below is your page-by-page review of what a website generated for you, plus automatic measurements and your original inputs. Now give the overall judgement.

=== YOU ===
{profile}

=== YOUR INPUTS ===
{inputs}

=== AUTOMATIC MEASUREMENTS ===
{measurements}

=== YOUR PART-BY-PART REVIEW ===
{parts}

=== RUBRIC ===
{rubric}

Return ONLY a JSON object:
{{
 "artifact_type": "what kind of output this is"{globals}
}}"""


def _compact_profile(p: Persona) -> str:
    bits = [p.short(), p.backstory.strip()[:700]]
    if p.goals:
        bits.append("Goals: " + "; ".join(p.goals))
    if p.frustrations:
        bits.append("Frustrations: " + "; ".join(p.frustrations))
    if p.language:
        bits.append("Language: " + "; ".join(f"{k}: {v}" for k, v in p.language.items()))
    if p.accessibility:
        bits.append("Accessibility: " + "; ".join(p.accessibility))
    return "\n".join(bits)


_PAGER = re.compile(r"^\s*(page\s*)?\d+\s*(/|of)\s*\d+\s*$|^[\s‹›<>«»←→]+$", re.I)


def _strip_boilerplate(captures: list[dict]) -> list[str]:
    texts = ["\n".join(l for l in c.get("text", "").splitlines() if not _PAGER.match(l)) for c in captures]
    if len(texts) < 3:
        return texts
    line_sets = [set(l.strip() for l in t.splitlines() if l.strip()) for t in texts]
    freq = Counter(l for s in line_sets for l in s)
    common = {l for l, c in freq.items() if c >= 0.6 * len(texts)}
    return ["\n".join(l for l in t.splitlines() if l.strip() and l.strip() not in common) for t in texts]


def _prose(text: str) -> str:
    """Keep sentence-like lines (UI chrome is mostly short labels)."""
    keep = []
    for line in text.splitlines():
        s = line.strip()
        if not s or _PAGER.match(s):
            continue
        if len(s.split()) >= 6 or (re.search(r"[.!?\"”]\s*$", s) and len(s.split()) >= 3):
            keep.append(s)
    return "\n".join(keep)


def _artifact_id(capture: dict) -> str:
    """Pages of one downloaded file share an artifact; on-page captures are grouped by page path."""
    u = urlparse(capture.get("url", ""))
    return f"file:{u.netloc}" if u.scheme == "file" else u.path


def _artifact_label(capture: dict, n: int) -> str:
    u = urlparse(capture.get("url", ""))
    if u.scheme == "file":
        name = u.netloc.split("_", 1)[-1]
        return f'the file "{name}" ({n} {"frames" if "frame" in u.path else "pages"})'
    title = re.sub(r"^auto:\s*", "", str(capture.get("label", ""))).strip()
    return f'the web page {u.path or "/"}' + (f' ("{title}")' if title else "")


def _compact_parts(parts: list) -> list:
    """Per-part reviews without verbatim text, so a long output's review fits in the synthesis prompt."""
    out = []
    for p in parts:
        if not isinstance(p, dict):
            continue
        out.append({k: v for k, v in {
            "output": p.get("artifact"), "part": p.get("part"), "reaction": str(p.get("reaction", ""))[:300],
            "picture": str(p.get("picture_description", ""))[:200],
            "problems": [{"criterion": q.get("criterion"), "severity": q.get("severity"), "evidence": str(q.get("evidence", ""))[:200]}
                         for q in (p.get("problems") or []) if isinstance(q, dict)],
            "suggested_change": str(p.get("suggested_change", ""))[:300],
        }.items() if v})
    return out


def _file_versions(captures: list[dict], prose: list[set]) -> dict[str, str]:
    """Map a file to the later file that regenerates it: same type and page count, and most pages' text unchanged."""
    files: dict[str, list[int]] = {}
    for i, c in enumerate(captures):
        if c.get("source") == "file":
            files.setdefault(_artifact_id(c), []).append(i)
    ids = list(files)
    newer: dict[str, str] = {}
    for n, a in enumerate(ids):
        for b in ids[n + 1:]:
            pa, pb = files[a], files[b]
            if len(pa) != len(pb) or Path(a).suffix.lower() != Path(b).suffix.lower():
                continue
            pairs = [(prose[x], prose[y]) for x, y in zip(pa, pb) if prose[x] or prose[y]]
            same = sum(1 for sx, sy in pairs if len(sx & sy) >= 0.8 * max(len(sx), len(sy)))
            if pairs and same >= 0.6 * len(pairs):
                newer[a] = b
                break
    return newer


def _supersede(captures: list[dict], texts: list[str]) -> tuple[list[int], dict[int, list[int]]]:
    """Captures to keep, and for each kept capture the earlier captures it replaces.

    Outputs are often captured while still being generated and again when finished, pages are captured
    again after the user edits them, and files are regenerated; the earlier state is not a separate part
    of the output, and counting it would duplicate every part. Screenshots of the browser's PDF viewer
    are dropped when the PDF itself was captured as a file.
    """
    prose = [set(_prose(t).splitlines()) for t in texts]
    where = [(urlparse(c.get("url", "")).netloc, urlparse(c.get("url", "")).path) for c in captures]
    file_names = {urlparse(c.get("url", "")).netloc.split("_", 1)[-1] for c in captures if c.get("source") == "file"}
    newer_file = _file_versions(captures, prose)
    keep: list[int] = []
    replaced: dict[int, list[int]] = {}
    for i, c in enumerate(captures):
        u = urlparse(c.get("url", ""))
        if u.scheme != "file" and Path(u.path).name in file_names and Path(u.path).suffix.lower() == ".pdf":
            continue
        aid = _artifact_id(c)
        if aid in newer_file:
            final = newer_file[aid]
            while final in newer_file:
                final = newer_file[final]
            page = u.path
            j = next((k for k, d in enumerate(captures) if _artifact_id(d) == final and urlparse(d.get("url", "")).path == page), None)
            if j is not None:
                replaced.setdefault(j, []).append(i)
            continue
        words = sum(len(ln.split()) for ln in prose[i])
        j = None
        if words >= 20:
            j = next((k for k in range(len(captures) - 1, i, -1)
                      if where[k] == where[i] and len(prose[i] & prose[k]) >= 0.8 * len(prose[i])), None)
        if j is None:
            keep.append(i)
        else:
            replaced.setdefault(j, []).append(i)
    return keep, {j: sorted(v) for j, v in replaced.items() if j in keep}


def _ahash(path: Path) -> Optional[int]:
    try:
        from PIL import Image

        px = list(Image.open(path).convert("L").resize((16, 16)).getdata())
    except Exception:
        return None
    avg = sum(px) / len(px)
    return sum(1 << i for i, p in enumerate(px) if p > avg)


def _redrawn(old: dict, new: dict, run_dir: Path) -> list[int]:
    """Positions of pictures that differ between two versions of a page (average hash, 256 bits)."""
    a = [im.get("path") for im in old.get("images") or []]
    b = [im.get("path") for im in new.get("images") or []]
    if not a or len(a) != len(b):
        return []
    out = []
    for k, (x, y) in enumerate(zip(a, b)):
        hx, hy = _ahash(run_dir / x), _ahash(run_dir / y)
        if hx is not None and hy is not None and bin(hx ^ hy).count("1") > 40:
            out.append(k)
    return out


def _changes_note(old: str, new: str, limit: int = 4) -> str:
    """What the user would notice changed between the first and the final version of a part."""
    a, b = _prose(old).splitlines(), _prose(new).splitlines()
    removed = [ln for ln in a if ln not in set(b)]
    added = [ln for ln in b if ln not in set(a)]
    if not removed and not added:
        return "the text did not change"
    out = []
    if removed:
        out.append("no longer there: " + " | ".join(f'"{ln[:220]}"' for ln in removed[:limit]))
    if added:
        out.append("new: " + " | ".join(f'"{ln[:220]}"' for ln in added[:limit]))
    return "; ".join(out)


def expected_names(persona: Persona, inputs: list[dict]) -> list[str]:
    names: list[str] = []
    dc = persona.domain_context or {}
    for key in ("children_in_story", "other_characters"):
        for c in dc.get(key, []) or []:
            if isinstance(c, dict) and c.get("name"):
                names.append(str(c["name"]))
    for i in inputs:
        f = str(i.get("field", "")).lower()
        v = str(i.get("value", ""))
        if any(k in f for k in ("name", "hero", "child", "character", "companion", "who")) and 1 < len(v) < 40:
            names.append(v)
    seen, out = set(), []
    for n in names:
        if n.lower() not in seen:
            seen.add(n.lower())
            out.append(n)
    return out


_NOT_READER = re.compile(r"teller|narrator|author|\byour\b|\bmy\b", re.I)


def reading_age(persona: Persona, inputs: list[dict]) -> Optional[float]:
    """The age the output is for: the last value entered in an age field that is not about the storyteller."""
    age = None
    for i in inputs:
        f = str(i.get("field", ""))
        if re.search(r"\bage\b|read", f, re.I) and not _NOT_READER.search(f):
            m = re.search(r"\d+(\.\d+)?", str(i.get("value") or ""))
            if m:
                age = float(m.group(0))
    if age is not None:
        return age
    ra = (persona.domain_context or {}).get("reading_age")
    try:
        return float(ra) if ra is not None else None
    except (TypeError, ValueError):
        return None


def _inputs_text(inputs: list[dict]) -> str:
    if not inputs:
        return "(no inputs were recorded)"
    lines = []
    for i in inputs:
        v = str(i.get("value", ""))
        trunc = f"  [NOTE: the site cut this to {i['truncated_to']} characters]" if i.get("truncated_to") else ""
        lines.append(f'- {i.get("field")}: "{v[:1500]}"{trunc}')
    return "\n".join(lines)


def _measurements_text(m: dict) -> str:
    r = m.get("overall_readability", {})
    lines = [
        f"- Readability of the prose: Flesch-Kincaid grade {r.get('fk_grade')}, Flesch reading ease {r.get('flesch_reading_ease')}, "
        f"{r.get('avg_sentence_words')} words/sentence, {r.get('words')} words in total."
        + (f" Requested reading age {m.get('reading_age_requested')}: {m.get('age_fit')}." if m.get("age_fit") else ""),
    ]
    if r.get("long_words"):
        lines.append("- Long words (4+ syllables): " + ", ".join(r["long_words"][:15]))
    for name, d in (m.get("names") or {}).items():
        s = f'- "{name}" appears {d["mentions"]} time(s)'
        if d["near_miss_variants"]:
            s += f"; near-miss spellings found: {', '.join(d['near_miss_variants'])}"
        lines.append(s)
    if m.get("unexpected_capitalised_names"):
        lines.append("- Other capitalised words/names not in your inputs: " + ", ".join(m["unexpected_capitalised_names"][:12]))
    if m.get("placeholders"):
        lines.append("- Template placeholders / glitches: " + ", ".join(m["placeholders"]))
    if m.get("repeated_sentences"):
        lines.append("- Repeated sentences: " + " | ".join(m["repeated_sentences"][:4]))
    if m.get("truncated_ending"):
        lines.append("- The text appears to end abruptly (no final punctuation).")
    if m.get("out_of_dictionary_words"):
        lines.append("- Words not in the dictionary (possible typos): " + ", ".join(m["out_of_dictionary_words"][:15]))
    return "\n".join(lines)


def _part_key(name: str) -> str:
    """'Page 9 (Scene 9)' and 'Scene 9' name the same part: key on the most specific numbered label."""
    n = str(name or "").lower()
    nums = re.findall(r"(scene|page|spread|chapter)\s*(\d+)", n)
    if nums:
        kind, num = next(((k, v) for k, v in nums if k == "scene"), nums[-1])
        return f"{kind} {int(num)}"
    return re.sub(r"[^a-z0-9]+", " ", n).strip()


def _merge_parts(parts: list, new: list) -> list:
    """Append a batch's parts, folding any part that was already reviewed into the earlier review."""
    out = list(parts)
    index = {_part_key(p.get("part", "")): p for p in out if isinstance(p, dict)}
    for p in new:
        if not isinstance(p, dict):
            continue
        prev = index.get(_part_key(p.get("part", "")))
        if prev is None:
            out.append(p)
            index[_part_key(p.get("part", ""))] = p
            continue
        prev["image_refs"] = list(dict.fromkeys((prev.get("image_refs") or []) + (p.get("image_refs") or [])))
        if not prev.get("picture_description") and p.get("picture_description"):
            prev["picture_description"] = p["picture_description"]
    return out


class OutputAssessor:
    def __init__(self, llm: LLMClient, run_dir: Path, max_images_per_call: int = 12, vision: bool = True):
        self.llm = llm
        self.run_dir = Path(run_dir)
        self.max_images = max_images_per_call
        self.vision = vision

    def assess(self, persona: Persona, inputs: list[dict], captures: list[dict], reactions: list[dict]) -> dict:
        if not captures:
            return {"skipped": True, "reason": "the session never reached any generated output"}
        texts = _strip_boilerplate(captures)
        kept, replaced = _supersede(captures, texts)
        superseded = [c.get("label", "") for i, c in enumerate(captures) if i not in kept]
        notes = {kept.index(j): (captures[old[0]].get("label", ""), _changes_note(texts[old[0]], texts[j]), captures[old[0]]) for j, old in replaced.items()}
        captures, texts = [captures[i] for i in kept], [texts[i] for i in kept]
        prose_parts = [{"part": c.get("label") or f"capture {i + 1}", "text": _prose(t), "artifact": _artifact_id(c)} for i, (c, t) in enumerate(zip(captures, texts))]
        names = expected_names(persona, inputs)
        age = reading_age(persona, inputs)
        m = metrics.analyse_parts(prose_parts, names, age)
        # Attach images: prefer element shots of pictures; fall back to viewport screenshots.
        images: list[tuple[str, str]] = []
        per_capture: list[int] = []
        for ci, c in enumerate(captures):
            before = len(images)
            imgs = c.get("images") or []
            if not self.vision:
                pass
            elif imgs:
                for im in imgs:
                    images.append((im["path"], f"capture {ci + 1}, {im['w']}x{im['h']}" + (f', alt "{im["alt"][:60]}"' if im.get("alt") else "")))
            else:
                for v in (c.get("views") or [])[:3]:
                    images.append((v, f"capture {ci + 1}, screenshot of the page"))
            per_capture.append(len(images) - before)
        artifact_blocks = []
        capture_images: list[list[int]] = []
        idx = 0
        for ci, (c, t) in enumerate(zip(captures, texts)):
            refs = []
            capture_images.append(list(range(idx, idx + per_capture[ci])))
            for _ in range(per_capture[ci]):
                idx += 1
                refs.append(f"I{idx}")
            if not self.vision:
                alts = [im.get("alt") for im in (c.get("images") or []) if im.get("alt")]
                if alts:
                    refs.append("(you cannot see the pictures; their alt text says: " + "; ".join(alts)[:300] + ")")
            change = ""
            if ci in notes:
                redrawn = _redrawn(notes[ci][2], c, self.run_dir)
                pics = [refs[k] if k < per_capture[ci] else f"picture {k + 1}" for k in redrawn]
                change = (f'\nthis is the final version; compared with the first version you saw ("{notes[ci][0]}"): {notes[ci][1]}'
                          + (f"; pictures redrawn since then: {', '.join(pics)}" if pics else ""))
                notes[ci] = (notes[ci][0], notes[ci][1] + (f"; pictures redrawn: {', '.join(pics)}" if pics else ""), notes[ci][2])
            artifact_blocks.append(
                f'[Capture {ci + 1}: "{c.get("label", "")}" - {c.get("url", "")}]\ntext:\n{t[:12000]}\npictures in this capture: {", ".join(refs) or "none"}{change}'
            )
        profile = _compact_profile(persona)
        inputs_txt = _inputs_text(inputs)
        meas_txt = _measurements_text(m)
        if reactions:
            meas_txt += "\n- Your in-the-moment reactions while viewing it: " + " | ".join(r["reaction"][:200] for r in reactions[:6])
        rubric = "\n".join(f"{k}: {v}" for k, v in CRITERIA.items())
        result: dict[str, Any] = {"measurements": m, "inputs": inputs, "expected_names": names, "reading_age": age,
                                  "superseded_captures": superseded, "version_changes": [{"part": captures[ci].get("label", ""), "since": n[0], "changes": n[1]}
                                                                                          for ci, n in notes.items()]}
        numbered = [(i, pth, d) for i, (pth, d) in enumerate(images)]
        try:
            if len(images) <= self.max_images:
                data = self._judge(persona.name, profile, inputs_txt, meas_txt, "\n\n".join(artifact_blocks), rubric, numbered, with_globals=True)
                result.update(data if isinstance(data, dict) else {})
            else:
                # Review each output (a web page, a PDF, ...) on its own so that "Page 3" of one is never taken for "Page 3" of another.
                groups: dict[str, list[int]] = {}
                for ci, c in enumerate(captures):
                    groups.setdefault(_artifact_id(c), []).append(ci)
                parts: list = []
                artifact_type = ""
                for gi, cis in enumerate(groups.values()):
                    label = _artifact_label(captures[cis[0]], len(cis))
                    pics = [numbered[k] for ci in cis for k in capture_images[ci]]
                    art_parts: list = []
                    for b in range(0, max(1, len(pics)), self.max_images):
                        batch = pics[b : b + self.max_images]
                        done = [str(p.get("part", "")) for p in art_parts if isinstance(p, dict)]
                        where = (f"You are now looking at pictures {', '.join(f'I{k + 1}' for k, _, _ in batch)} of it; review the parts these pictures belong to, "
                                 "plus any text-only parts in between." if batch else "It has no pictures; review its text.")
                        header = (f"(The website produced {len(groups)} different outputs for you. This is output {gi + 1} of {len(groups)}: {label}. {where}"
                                  + (f" You have ALREADY reviewed these parts of it - do not review them again: {'; '.join(done)}." if done else "") + ")\n\n")
                        data = self._judge(persona.name, profile, inputs_txt, meas_txt, header + "\n\n".join(artifact_blocks[ci] for ci in cis), rubric, batch,
                                           with_globals=False)
                        new = (data or {}).get("parts", []) if isinstance(data, dict) else []
                        for p in new:
                            if isinstance(p, dict):
                                p["artifact"] = label
                        art_parts = _merge_parts(art_parts, new)
                        artifact_type = artifact_type or (data or {}).get("artifact_type", "")
                    parts += art_parts
                synth = self._synthesise(persona.name, profile, inputs_txt, meas_txt, parts, rubric)
                result.update(synth if isinstance(synth, dict) else {})
                result["parts"] = parts
                result.setdefault("artifact_type", artifact_type)
        except LLMError as e:
            result["error"] = str(e)
        for p in result.get("parts", []) or []:
            if isinstance(p, dict) and p.get("text"):
                prose = _prose(str(p["text"]))
                if len(prose.split()) >= 8:
                    r = metrics.readability(prose)
                    p["metrics"] = {k: r.get(k) for k in ("words", "avg_sentence_words", "fk_grade", "flesch_reading_ease")}
        result["images"] = [{"ref": f"I{i + 1}", "path": pth, "desc": d} for i, (pth, d) in enumerate(images)]
        return result

    def _judge(self, name, profile, inputs_txt, meas_txt, artifact, rubric, images: list[tuple[int, str, str]], with_globals: bool):
        task = PARTS_TASK % (GLOBAL_FIELDS if with_globals else "")
        prompt = JUDGE_TEMPLATE.format(name=name, profile=profile, inputs=inputs_txt, measurements=meas_txt, artifact=artifact, rubric=rubric, task=task)
        content: list[dict] = [{"type": "text", "text": prompt}]
        if self.llm.supports_images():
            for i, path, desc in images:
                content.append({"type": "text", "text": f"[I{i + 1}] {desc}"})
                content.append(image_part((self.run_dir / path).read_bytes()))
        data, _ = self.llm.chat_json(
            [{"role": "user", "content": content}], purpose="output_assessment", max_tokens=16000, temperature=0.3, reasoning_effort="medium"
        )
        return data

    def _synthesise(self, name, profile, inputs_txt, meas_txt, parts, rubric):
        prompt = SYNTH_TEMPLATE.format(
            name=name, profile=profile, inputs=inputs_txt, measurements=meas_txt,
            parts=json.dumps(_compact_parts(parts), ensure_ascii=False)[:90000], rubric=rubric, globals=GLOBAL_FIELDS,
        )
        data, _ = self.llm.chat_json([{"role": "user", "content": prompt}], purpose="output_synthesis", max_tokens=8000, temperature=0.3, reasoning_effort="medium")
        return data
