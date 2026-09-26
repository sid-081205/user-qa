"""Deterministic measurements of generated text, used to ground the LLM judge.

LLM judges are known to be biased and to overlook surface errors (Zheng et al.
2023; Wang et al. 2023), so the assessor first runs cheap, reproducible checks
and passes their findings to the judge as tool evidence:

* readability: Flesch Reading Ease (Flesch 1948) and Flesch-Kincaid grade
  (Kincaid et al. 1975), compared with the requested reading age,
* input fidelity: whether names/objects the user typed appear in the output,
  and near-miss spellings of those names,
* generation glitches: template placeholders, repeated sentences, truncated
  endings, out-of-dictionary words.
"""
from __future__ import annotations

import re
from difflib import SequenceMatcher
from functools import lru_cache
from pathlib import Path
from typing import Iterable, Optional

_WORD = re.compile(r"[A-Za-z][A-Za-z'\-]*")
_SENT = re.compile(r"[^.!?]+[.!?]+|[^.!?]+$")
PLACEHOLDER_PATTERNS = [
    r"\{\{[^}]*\}\}",
    r"\{[a-z_]+\}",
    r"\[(?:name|child|insert|placeholder)[^\]]*\]",
    r"\bundefined\b",
    r"\bnull\b",
    r"\bNaN\b",
    r"lorem ipsum",
    r"\bTODO\b",
    r"\[object Object\]",
]
STOP_CAPS = {
    "The", "A", "An", "And", "But", "Then", "One", "Once", "When", "She", "He", "They", "It", "Her", "His", "Their",
    "We", "I", "You", "In", "On", "At", "As", "So", "With", "For", "Of", "To", "Page", "Chapter", "End", "Every",
    "That", "This", "There", "Here", "What", "Where", "Who", "Why", "How", "Mum", "Dad", "Mama", "Papa", "Grandma",
    "Grandpa", "Granny", "Nana", "Uncle", "Aunt", "Auntie", "Mr", "Mrs", "Ms", "Dr", "Oh", "Yes", "No", "Not", "All",
}


def syllables(word: str) -> int:
    w = word.lower().strip("'")
    if len(w) <= 3:
        return 1
    w = re.sub(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$", "", w)
    w = re.sub(r"^y", "", w)
    groups = re.findall(r"[aeiouy]{1,2}", w)
    return max(1, len(groups))


def readability(text: str) -> dict:
    words = _WORD.findall(text)
    sents = [s for s in _SENT.findall(text) if _WORD.search(s)]
    n_w, n_s = len(words), max(1, len(sents))
    if n_w == 0:
        return {"words": 0, "sentences": 0}
    syl = sum(syllables(w) for w in words)
    poly = sum(1 for w in words if syllables(w) >= 3)
    fre = 206.835 - 1.015 * (n_w / n_s) - 84.6 * (syl / n_w)
    fk = 0.39 * (n_w / n_s) + 11.8 * (syl / n_w) - 15.59
    return {
        "words": n_w,
        "sentences": len(sents),
        "avg_sentence_words": round(n_w / n_s, 1),
        "flesch_reading_ease": round(fre, 1),
        "fk_grade": round(fk, 1),
        "polysyllabic_ratio": round(poly / n_w, 3),
        "long_words": sorted({w for w in words if syllables(w) >= 4}, key=str.lower)[:25],
    }


def age_fit(fk_grade: Optional[float], reading_age: Optional[float]) -> Optional[str]:
    """Rough check: US grade ~= age - 5 (grade 1 at age 6)."""
    if fk_grade is None or reading_age is None:
        return None
    target = max(0.0, float(reading_age) - 5.0)
    if fk_grade <= target + 1.5:
        return "appropriate"
    if fk_grade <= target + 3.5:
        return "somewhat difficult for the target age"
    return "too difficult for the target age"


@lru_cache(maxsize=1)
def _dictionary() -> frozenset:
    words: set[str] = set()
    for f in ("/usr/share/dict/british-english", "/usr/share/dict/american-english", "/usr/share/dict/words"):
        p = Path(f)
        if p.exists():
            words.update(w.strip().lower() for w in p.read_text(errors="ignore").splitlines())
    return frozenset(words)


def unknown_words(text: str, known_names: Iterable[str] = ()) -> list[str]:
    d = _dictionary()
    if not d:
        return []
    names = {n.lower() for n in known_names}
    out = []
    for w in set(_WORD.findall(text)):
        lw = w.lower().strip("'-")
        if len(lw) < 4 or lw in d or lw in names or w[0].isupper():
            continue
        base = re.sub(r"(?:'s|s|es|ed|ing|ly|er|est)$", "", lw)
        if base in d or base + "e" in d:
            continue
        out.append(w)
    return sorted(out)[:30]


def placeholders(text: str) -> list[str]:
    hits = []
    for p in PLACEHOLDER_PATTERNS:
        hits += [m.group(0) for m in re.finditer(p, text, re.I)]
    return hits[:20]


def repeated_sentences(parts: list[str], min_words: int = 6) -> list[str]:
    seen: dict[str, int] = {}
    reps = []
    for i, part in enumerate(parts):
        for s in _SENT.findall(part):
            norm = re.sub(r"\W+", " ", s.lower()).strip()
            if len(norm.split()) < min_words:
                continue
            if norm in seen and seen[norm] != i:
                reps.append(s.strip())
            seen.setdefault(norm, i)
    return reps[:10]


def truncated_ending(text: str) -> bool:
    t = text.strip()
    if not t:
        return False
    last_line = [l for l in t.splitlines() if _WORD.search(l)][-1].strip()
    return len(last_line.split()) >= 5 and not re.search(r"[.!?\"'”’)…]$", last_line)


def name_fidelity(output_text: str, expected_names: Iterable[str]) -> dict:
    """For each expected name: exact mentions and near-miss variants (possible misspellings)."""
    caps = [w for w in _WORD.findall(output_text) if w[0].isupper() and w not in STOP_CAPS]
    res = {}
    for name in {n.strip() for n in expected_names if n and len(n.strip()) >= 2}:
        first = name.split()[-1] if name.split()[0].lower() in {"grandma", "grandpa", "uncle", "aunt", "mama", "dad"} else name.split()[0]
        exact = len(re.findall(rf"\b{re.escape(first)}\b", output_text))
        variants = sorted(
            {
                c
                for c in caps
                if c != first and c[0].lower() == first[0].lower() and 0.6 <= SequenceMatcher(None, c.lower(), first.lower()).ratio() < 1.0 and abs(len(c) - len(first)) <= 2
            }
        )
        res[name] = {"token": first, "mentions": exact, "near_miss_variants": variants[:5]}
    return res


def unexpected_names(output_text: str, expected_names: Iterable[str], min_count: int = 1) -> list[str]:
    exp = {t.lower() for n in expected_names for t in re.findall(r"[A-Za-z]+", n)}
    counts: dict[str, int] = {}
    for m in re.finditer(r"(?<![.!?]\s)(?<!^)\b([A-Z][a-z]{2,})\b", output_text, re.M):
        w = m.group(1)
        if w in STOP_CAPS or w.lower() in exp:
            continue
        counts[w] = counts.get(w, 0) + 1
    return sorted([w for w, c in counts.items() if c >= min_count], key=lambda w: -counts[w])[:15]


def analyse_parts(parts: list[dict], expected_names: Iterable[str], reading_age: Optional[float]) -> dict:
    """``parts`` = [{"part": "Page 1", "text": "..."}]."""
    expected_names = list(expected_names)
    full = "\n".join(p.get("text", "") for p in parts)
    overall = readability(full)
    per_part = []
    for p in parts:
        r = readability(p.get("text", ""))
        per_part.append({"part": p.get("part"), **{k: r.get(k) for k in ("words", "avg_sentence_words", "fk_grade", "flesch_reading_ease")}})
    return {
        "overall_readability": overall,
        "age_fit": age_fit(overall.get("fk_grade"), reading_age),
        "reading_age_requested": reading_age,
        "per_part": per_part,
        "names": name_fidelity(full, expected_names),
        "unexpected_capitalised_names": unexpected_names(full, expected_names),
        "placeholders": placeholders(full),
        "repeated_sentences": repeated_sentences([p.get("text", "") for p in parts]),
        "truncated_ending": truncated_ending(full),
        "out_of_dictionary_words": unknown_words(full, expected_names),
    }
