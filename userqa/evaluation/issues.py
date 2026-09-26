"""Flatten per-page issue reports and merge site-wide duplicates.

A site-wide defect (e.g. a pale footer) is reported on every page it appears on.
For counting and ranking we cluster near-duplicates (same code family, similar
wording) so one defect is counted once, while keeping every page it was seen on.
"""
from __future__ import annotations

import re
from typing import Any

_STOP = set(
    "a an the and or of to in on for with is are was be it this that these those my me i you your our its at by from as "
    "not no so very too than then there their they them just only also can could would should will may might has have had "
    "do does did which who what when where why how page site website text".split()
)


def _sev(i: dict) -> int:
    try:
        return int(i.get("severity", 0))
    except (TypeError, ValueError):
        return 0


def _family(code: Any) -> str:
    return re.split(r"[\s/,;|]+", str(code or "?").strip().upper())[0] or "?"


def _stem(w: str) -> str:
    for suf in ("ing", "ed", "es", "s"):
        if len(w) > 4 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def _tokens(i: dict) -> set[str]:
    text = f"{i.get('title', '')} {i.get('title', '')} {str(i.get('evidence', ''))[:160]}"
    return {_stem(w) for w in re.findall(r"[a-z0-9£$]+", text.lower()) if w not in _STOP and len(w) > 2}


def flatten_issues(pages: dict) -> list[dict]:
    out = []
    for key, p in pages.items():
        rv = p.get("review") or {}
        for src, lst in (("first_visit", rv.get("issues") or []), ("later", p.get("later_issues") or [])):
            for i in lst:
                if isinstance(i, dict) and i.get("title"):
                    out.append({**i, "page": rv.get("page_name") or p.get("title"), "page_key": key, "source": src})
    return out


def cluster_issues(issues: list[dict], threshold: float = 0.3) -> list[dict]:
    """Greedy single-pass clustering by Jaccard similarity of content tokens within a code family."""
    clusters: list[dict] = []
    for i in sorted(issues, key=lambda x: -_sev(x)):
        toks, fam = _tokens(i), _family(i.get("code"))
        best, best_sim = None, 0.0
        for c in clusters:
            sim = len(toks & c["_tokens"]) / max(1, len(toks | c["_tokens"]))
            if (c["family"] == fam and sim >= threshold) or sim >= 0.6:
                if sim > best_sim:
                    best, best_sim = c, sim
        if best is None:
            clusters.append({"family": fam, "_tokens": set(toks), "representative": i, "members": [i]})
        else:
            best["members"].append(i)
            best["_tokens"] |= toks
    out = []
    for c in clusters:
        rep = dict(c["representative"])
        pages = []
        for m in c["members"]:
            if m.get("page") and m["page"] not in pages:
                pages.append(m["page"])
        rep.update(
            pages=pages,
            occurrences=len(c["members"]),
            max_severity=max(_sev(m) for m in c["members"]),
            mean_severity=round(sum(_sev(m) for m in c["members"]) / len(c["members"]), 2),
        )
        out.append(rep)
    return sorted(out, key=lambda r: (-r["max_severity"], -r["occurrences"]))
