"""Score simulated-user sessions against StoryHearth's seeded defects.

    python experiments/score_ground_truth.py runs/suite/main            # every run under a suite
    python experiments/score_ground_truth.py runs/pilot/<run-dir> ...   # individual runs

Findings are the agent's *formal* reports only: page-review issues and later issues (UX) and the
per-part problems, input-fidelity misses and safety concerns of the output assessment (output).
Think-aloud mentions do not count.

Each finding is matched to at most one seeded defect by
  * an LLM judge (strict: same element/content and same kind of problem), cached in
    <run>/gt_judge.json so re-scoring is free, and
  * a transparent keyword baseline (same kind, same page for UX defects, any defect keyword).
Unmatched findings are classed by the judge as valid-but-unseeded or incorrect; repeat matches of
an already-found defect are duplicates.

Recall is reported raw (over all defects) and exposure-adjusted (over defects the agent could have
met: it visited the page / triggered the condition / the defect's text was in the captured output).
A deterministic baseline records which output defects the rule-based text metrics alone flag.
Writes <run>/gt_scores.json; prints one line per run.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from userqa.evaluation.issues import flatten_issues  # noqa: E402

GT_PATH = ROOT / "demo_sites/storyhearth/ground_truth.json"

JUDGE_SYSTEM = """You score an automated usability evaluation against a list of KNOWN defects that were deliberately
seeded into a test website. For every numbered finding decide which known defect (if any) it reports.
Be strict: a finding matches a defect only if it clearly describes the same underlying problem - the same
element or content AND the same kind of problem. Being on the same page or touching a related theme is
not enough (e.g. "the Next button is small" does not match "the book title has a typo").
A finding may match at most one defect; pick the closest if it clearly covers one. If a finding matches
none, classify it as:
  "valid_unseeded" - a plausible, specific problem a real user could have that is not in the list, or
  "incorrect"      - vague, not actually a problem, contradicted by its own evidence, or likely invented.
Reply with JSON only: {"judgements": [{"f": "F1", "defect": "U2" or null, "class": "matched" | "valid_unseeded" | "incorrect"}]}
covering every finding exactly once."""


def page_file(ref: str) -> str:
    s = (ref or "").split(" | ")[0]
    path = urlparse(s).path if "://" in s else ("/" + s.split("/", 1)[1] if "/" in s else "/")
    return path.split("#")[0].rstrip("/").split("/")[-1] or "index.html"


def load_run(run_dir: Path) -> dict:
    session = json.loads((run_dir / "session.json").read_text())
    assessment = json.loads((run_dir / "output_assessment.json").read_text()) if (run_dir / "output_assessment.json").exists() else {}
    trace = [json.loads(ln) for ln in (run_dir / "trace.jsonl").read_text().splitlines()] if (run_dir / "trace.jsonl").exists() else []
    captures = []
    for c in session.get("captures") or []:
        t = run_dir / c.get("dir", "") / "text.txt"
        captures.append(t.read_text() if c.get("dir") and t.exists() else "")
    return {"session": session, "assessment": assessment, "trace": trace, "capture_texts": captures}


def findings_for(run: dict) -> list[dict]:
    out = []
    pages = run["session"].get("pages") or {}
    for i in flatten_issues(pages):
        step = i.get("step") if i.get("source") == "later" else (pages.get(i.get("page_key")) or {}).get("first_step")
        out.append({
            "kind": "ux", "where": page_file(i.get("page_key", "")), "page_name": i.get("page"), "title": i.get("title", ""),
            "evidence": str(i.get("evidence", "")), "why": str(i.get("why_it_matters_to_me", "")), "code": i.get("code"),
            "severity": i.get("severity"), "source": i.get("source"), "step": step,
            "verified_quote": (i.get("evidence_check") or {}).get("verified"),
        })
    a = run["assessment"] or {}
    for p in a.get("parts") or []:
        for pr in p.get("problems") or []:
            out.append({"kind": "output", "where": p.get("part", ""), "title": pr.get("criterion", ""),
                        "evidence": str(pr.get("evidence", "")), "severity": pr.get("severity"), "source": "output_part"})
    fid = a.get("input_fidelity") or {}
    for key in ("missing", "changed"):
        for x in fid.get(key) or []:
            out.append({"kind": "output", "where": "whole book", "title": f"input fidelity: {key}", "evidence": str(x), "source": f"fidelity_{key}"})
    for x in a.get("safety_concerns") or []:
        out.append({"kind": "output", "where": "whole book", "title": "safety concern", "evidence": str(x), "source": "safety"})
    for n, f in enumerate(out, 1):
        f["fid"] = f"F{n}"
    return out


def exposure(defects: list[dict], run: dict) -> dict[str, bool]:
    visited = {page_file(t.get("url", "")) for t in run["trace"]} | {page_file(k) for k in (run["session"].get("pages") or {})}
    typed_long = any(
        re.search(r"memory|idea|story", str(i.get("field", "")), re.I) and (len(str(i.get("value", ""))) > 200 or i.get("truncated_to"))
        for i in run["session"].get("inputs") or []
    )
    caps = run["capture_texts"]
    out = {}
    for d in defects:
        if d["kind"] == "output":
            need = int(d.get("signature_min_captures", 1))
            out[d["id"]] = all(sum(1 for c in caps if s.lower() in c.lower()) >= need for s in d.get("signature") or ["\0"])
            continue
        cond = d.get("exposure")
        if cond == "idea_truncated":
            out[d["id"]] = typed_long
        elif cond and cond.startswith("visited:"):
            out[d["id"]] = cond.split(":", 1)[1] in visited
        else:
            out[d["id"]] = bool(visited) if d["page"] == "*" else d["page"] in visited
    return out


def keyword_match(f: dict, defects: list[dict]) -> str | None:
    text = f"{f['title']} {f['evidence']} {f.get('why', '')}".lower()
    best, hits = None, 0
    for d in defects:
        if d["kind"] != f["kind"]:
            continue
        if d["kind"] == "ux" and d["page"] != "*" and d["page"] != f["where"]:
            continue
        n = sum(1 for k in d.get("keywords") or [] if k.lower() in text)
        if n > hits:
            best, hits = d["id"], n
    return best


def deterministic_baseline(assessment: dict) -> list[str]:
    m = (assessment or {}).get("measurements") or {}
    found = []
    if any(w.lower() == "adventrue" for w in m.get("out_of_dictionary_words") or []):
        found.append("O1")
    if m.get("placeholders"):
        found.append("O2")
    names = m.get("names") or {}
    if any(v.get("near_miss_variants") for v in names.values()):
        found.append("O3")
    if any(v.get("mentions") == 0 for v in names.values()):
        found.append("O5")
    if "Bartholomew" in (m.get("unexpected_capitalised_names") or []):
        found.append("O6")
    if str(m.get("age_fit", "")).startswith("too difficult"):
        found.append("O8")
    if m.get("repeated_sentences"):
        found.append("O12")
    if m.get("truncated_ending"):
        found.append("O13")
    return found


def judge(findings: list[dict], defects: list[dict], llm, cache: Path, rejudge: bool) -> dict[str, dict]:
    if cache.exists() and not rejudge:
        data = json.loads(cache.read_text())
        if data.get("n_findings") == len(findings):
            return {j["f"]: j for j in data["judgements"]}
    dlist = "\n".join(f'{d["id"]} [{d["kind"]}; {d.get("page") or d.get("part")}] {d["title"]}: {d["description"]}' for d in defects)
    judgements: dict[str, dict] = {}
    for start in range(0, len(findings), 45):
        chunk = findings[start : start + 45]
        flist = "\n".join(
            f'{f["fid"]} [{f["kind"]}; {f["where"]}] {f["title"]}: {f["evidence"][:280]}' + (f' (why: {f["why"][:120]})' if f.get("why") else "")
            for f in chunk
        )
        msgs = [{"role": "system", "content": JUDGE_SYSTEM},
                {"role": "user", "content": f"KNOWN DEFECTS:\n{dlist}\n\nFINDINGS:\n{flist}"}]
        data, meta = llm.chat_json(msgs, purpose="gt_judge", temperature=0.0, max_tokens=5000)
        for j in (data.get("judgements") if isinstance(data, dict) else data) or []:
            if isinstance(j, dict) and j.get("f"):
                judgements[str(j["f"]).strip()] = j
    valid = {d["id"] for d in defects}
    for f in findings:
        j = judgements.setdefault(f["fid"], {"f": f["fid"], "defect": None, "class": "incorrect", "missing": True})
        if j.get("defect") not in valid:
            j["defect"] = None
        if j["defect"] and j.get("class") != "matched":
            j["class"] = "matched"
        if not j["defect"] and j.get("class") not in ("valid_unseeded", "incorrect"):
            j["class"] = "incorrect"
    cache.write_text(json.dumps({"n_findings": len(findings), "model": llm.model, "judgements": list(judgements.values())}, indent=1))
    return judgements


def score_run(run_dir: Path, gt: dict, llm, rejudge: bool = False) -> dict:
    defects = gt["defects"]
    run = load_run(run_dir)
    findings = findings_for(run)
    exp = exposure(defects, run)
    judged = judge(findings, defects, llm, run_dir / "gt_judge.json", rejudge) if llm and findings else {}
    kinds = {"ux": [d["id"] for d in defects if d["kind"] == "ux"], "output": [d["id"] for d in defects if d["kind"] == "output"]}
    det_judge: dict[str, list[str]] = {}
    det_kw: dict[str, list[str]] = {}
    classes = {"matched": 0, "duplicate": 0, "valid_unseeded": 0, "incorrect": 0}
    first_step: dict[str, int] = {}
    for f in findings:
        kw = keyword_match(f, defects)
        f["keyword_defect"] = kw
        if kw:
            det_kw.setdefault(kw, []).append(f["fid"])
        j = judged.get(f["fid"])
        if not j:
            continue
        f["judge_defect"], f["judge_class"] = j.get("defect"), j.get("class")
        if j.get("defect"):
            if j["defect"] in det_judge:
                classes["duplicate"] += 1
                f["judge_class"] = "duplicate"
            else:
                classes["matched"] += 1
            det_judge.setdefault(j["defect"], []).append(f["fid"])
            if f.get("step") is not None:
                first_step[j["defect"]] = min(first_step.get(j["defect"], 10**6), int(f["step"]))
        else:
            classes[j["class"]] += 1

    def recall(detected: dict, kind: str) -> dict:
        ids = kinds[kind]
        exposed = [i for i in ids if exp[i]]
        hit = [i for i in ids if i in detected]
        return {"detected": hit, "raw": round(len(hit) / len(ids), 3), "exposed_n": len(exposed),
                "exposure_adjusted": round(len([i for i in hit if exp[i]]) / len(exposed), 3) if exposed else None}

    n = len(findings)
    det_base = deterministic_baseline(run["assessment"])
    cfg = json.loads((run_dir / "config.json").read_text())
    result = {
        "run": run_dir.name,
        "persona": cfg.get("persona"),
        "vision": cfg.get("vision", True),
        "model": cfg.get("model"),
        "status": run["session"].get("status"),
        "steps": run["session"].get("steps"),
        "n_findings": n,
        "n_findings_by_kind": {k: sum(1 for f in findings if f["kind"] == k) for k in ("ux", "output")},
        "exposed": exp,
        "judge": {"ux": recall(det_judge, "ux"), "output": recall(det_judge, "output"), "classes": classes,
                  "precision_strict": round((classes["matched"] + classes["duplicate"]) / n, 3) if n and judged else None,
                  "precision_lenient": round((classes["matched"] + classes["duplicate"] + classes["valid_unseeded"]) / n, 3) if n and judged else None,
                  "first_step": first_step},
        "keyword": {"ux": recall(det_kw, "ux"), "output": recall(det_kw, "output")},
        "deterministic_output_baseline": {"detected": det_base, "raw": round(len(det_base) / len(kinds["output"]), 3)},
        "findings": findings,
    }
    (run_dir / "gt_scores.json").write_text(json.dumps(result, indent=1, ensure_ascii=False))
    return result


def discover_runs(paths: list[str]) -> list[Path]:
    runs = []
    for p in map(Path, paths):
        if (p / "session.json").exists():
            runs.append(p)
        else:
            runs += sorted(q.parent for q in p.glob("*/session.json"))
    return runs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--no-judge", action="store_true", help="keyword baseline only (no LLM calls)")
    ap.add_argument("--rejudge", action="store_true")
    ap.add_argument("--judge-model")
    a = ap.parse_args()
    gt = json.loads(GT_PATH.read_text())
    llm = None
    if not a.no_judge:
        from userqa.llm import DEFAULT_MODEL, LLMClient
        from userqa.runner import load_env_file

        load_env_file()
        llm = LLMClient(model=a.judge_model or DEFAULT_MODEL, fallbacks=[], max_calls=400, temperature=0.0)
    for run_dir in discover_runs(a.paths):
        try:
            r = score_run(run_dir, gt, llm, a.rejudge)
        except Exception as e:  # keep scoring the rest of the suite
            print(f"{run_dir.name}: ERROR {e}")
            continue
        j, k = r["judge"], r["keyword"]
        print(f"{r['run']}: findings={r['n_findings']} | judge UX {len(j['ux']['detected'])}/17 (exp-adj {j['ux']['exposure_adjusted']}) "
              f"output {len(j['output']['detected'])}/14 (exp-adj {j['output']['exposure_adjusted']}) P={j['precision_strict']}/{j['precision_lenient']} "
              f"| keyword UX {len(k['ux']['detected'])} output {len(k['output']['detected'])} | deterministic output {len(r['deterministic_output_baseline']['detected'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
