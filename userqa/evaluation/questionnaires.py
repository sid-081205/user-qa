"""Standardised post-session questionnaires and retrospective interview.

* SUS - System Usability Scale (Brooke 1996), scored 0-100, graded with the
  Sauro-Lewis curved grading scale (Sauro & Lewis 2016).
* UEQ-S - short User Experience Questionnaire (Schrepp et al. 2017): pragmatic
  and hedonic quality on -3..+3.
* NPS-style likelihood to recommend (0-10).
* Retrospective probing interview (cf. UXAgent's "agent interview", Lu et al. 2025).

LLM survey answers show response biases (Tjuatja et al. 2024; Dominguez-Olmedo
et al. 2024), so we (a) ask for a one-line justification before each rating,
(b) keep SUS's alternating item polarity and (c) compute an acquiescence index
that flags agreeing with both positive and negative items.
"""
from __future__ import annotations

import json
from typing import Any

from ..llm import LLMClient, LLMError
from ..personas.schema import Persona

SUS_ITEMS = [
    "I think that I would like to use this website frequently.",
    "I found the website unnecessarily complex.",
    "I thought the website was easy to use.",
    "I think that I would need the support of a technical person to be able to use this website.",
    "I found the various functions in this website were well integrated.",
    "I thought there was too much inconsistency in this website.",
    "I would imagine that most people would learn to use this website very quickly.",
    "I found the website very cumbersome (awkward) to use.",
    "I felt very confident using the website.",
    "I needed to learn a lot of things before I could get going with this website.",
]
UEQS_ITEMS = [
    ("obstructive", "supportive", "pragmatic"),
    ("complicated", "easy", "pragmatic"),
    ("inefficient", "efficient", "pragmatic"),
    ("confusing", "clear", "pragmatic"),
    ("boring", "exciting", "hedonic"),
    ("not interesting", "interesting", "hedonic"),
    ("conventional", "inventive", "hedonic"),
    ("usual", "leading edge", "hedonic"),
]
INTERVIEW = [
    ("purpose", "In one or two sentences, what is this website for, and who is it for?"),
    ("worst_moment", "What was the most frustrating or confusing moment, and why?"),
    ("best_moment", "What was the best moment?"),
    ("abandon", "Was there any point where, in real life, you would have given up? Where and why?"),
    ("missing", "What did you expect to find or be able to do that wasn't there?"),
    ("trust", "Did you trust this website with your information (and your family's)? Why or why not?"),
    ("willingness_to_pay", "Would you pay for this? How much would feel fair, and what would make you pay more?"),
    ("output_verdict", "If the site produced something for you, how do you feel about it overall?"),
]

SUS_GRADES = [  # Sauro & Lewis (2016) curved grading scale
    (84.1, "A+"), (80.8, "A"), (78.9, "A-"), (77.2, "B+"), (74.1, "B"), (72.6, "B-"),
    (71.1, "C+"), (65.0, "C"), (62.7, "C-"), (51.7, "D"), (0.0, "F"),
]

DEBRIEF_TEMPLATE = """You are {name}. You have just finished a session on a website for a usability study. Answer the post-session questionnaire honestly and in character, based ONLY on what you experienced (summarised below). Real participants are not polite: if it was hard, say so; if it was good, say so.

=== YOU ===
{profile}

=== WHAT HAPPENED IN YOUR SESSION ===
{journey}

=== WHAT YOU THOUGHT OF THE OUTPUT (if any) ===
{output}

=== QUESTIONNAIRE ===
Part A - SUS. For each statement give a one-line reason, then a rating 1-5 (1 = strongly disagree, 5 = strongly agree):
{sus}

Part B - For each word pair, rate 1-7 where 1 = the left word fits completely and 7 = the right word fits completely:
{ueq}

Part C - How likely are you to recommend this website to a friend or family member? 0-10.

Part D - Interview (answer in character, 1-3 sentences each):
{interview}

Part E - As a study participant, list the changes you would most like the website to make, most important first, each with the page it concerns and why it matters to you.

Return ONLY a JSON object:
{{
 "sus": [{{"item": 1, "reason": "...", "rating": 1-5}}, ... 10 items],
 "ueq_s": [{{"pair": "obstructive/supportive", "rating": 1-7}}, ... 8 items],
 "nps": 0-10,
 "interview": {{{interview_keys}}},
 "recommendations": [{{"change": "...", "page": "...", "why": "...", "priority": "high|medium|low"}}],
 "one_line_verdict": "in character"
}}"""


def score_sus(ratings: list[int]) -> dict:
    if len(ratings) != 10 or any(r is None for r in ratings):
        return {"score": None, "error": "need 10 ratings"}
    r = [max(1, min(5, int(x))) for x in ratings]
    total = sum((r[i] - 1) if i % 2 == 0 else (5 - r[i]) for i in range(10))
    score = total * 2.5
    grade = next(g for thr, g in SUS_GRADES if score >= thr)
    pos, neg = [r[i] for i in range(0, 10, 2)], [r[i] for i in range(1, 10, 2)]
    # Acquiescence: agreeing (>=4) with a positive AND its paired negative item is logically inconsistent.
    inconsistent_pairs = sum(1 for p, n in zip(pos, neg) if p >= 4 and n >= 4) + sum(1 for p, n in zip(pos, neg) if p <= 2 and n <= 2)
    return {
        "score": score,
        "grade": grade,
        "above_average_68": score >= 68,
        "mean_positive_items": sum(pos) / 5,
        "mean_negative_items": sum(neg) / 5,
        "inconsistent_pairs": inconsistent_pairs,
        "consistency_flag": inconsistent_pairs >= 2,
    }


def score_ueqs(ratings: list[int]) -> dict:
    if len(ratings) != 8:
        return {"pragmatic": None, "hedonic": None}
    v = [max(1, min(7, int(x))) - 4 for x in ratings]
    prag, hed = sum(v[:4]) / 4, sum(v[4:]) / 4
    return {"pragmatic": prag, "hedonic": hed, "overall": (prag + hed) / 2}


def run_debrief(llm: LLMClient, persona: Persona, journey: str, output_summary: str) -> dict:
    prompt = DEBRIEF_TEMPLATE.format(
        name=persona.name,
        profile=persona.profile_text() if not persona.baseline else "a typical adult web user",
        journey=journey[:30000],
        output=output_summary[:8000] or "(the session did not reach any generated output)",
        sus="\n".join(f"{i + 1}. {s}" for i, s in enumerate(SUS_ITEMS)),
        ueq="\n".join(f"{i + 1}. {a} / {b}" for i, (a, b, _) in enumerate(UEQS_ITEMS)),
        interview="\n".join(f"- {k}: {q}" for k, q in INTERVIEW),
        interview_keys=", ".join(f'"{k}": "..."' for k, _ in INTERVIEW),
    )
    try:
        data, _ = llm.chat_json([{"role": "user", "content": prompt}], purpose="debrief", max_tokens=6000, temperature=0.5)
    except LLMError as e:
        return {"error": str(e)}
    if not isinstance(data, dict):
        return {"error": "bad debrief format"}
    sus_items = sorted([x for x in data.get("sus", []) if isinstance(x, dict)], key=lambda x: int(x.get("item", 0) or 0))
    ratings = [_int(x.get("rating")) for x in sus_items][:10]
    data["sus_score"] = score_sus(ratings)
    ueq = [_int(x.get("rating")) for x in data.get("ueq_s", []) if isinstance(x, dict)][:8]
    data["ueq_s_score"] = score_ueqs(ueq) if all(u is not None for u in ueq) else {}
    return data


def _int(v: Any):
    try:
        return int(round(float(v)))
    except (TypeError, ValueError):
        return None


def journey_digest(trace: list[dict], pages: dict, waits: list[dict]) -> str:
    """The session as the participant lived it, for the debrief and the fidelity audit.

    A step's events (a file the site gave them and they read, a pop-up, a new tab) are what the browser told the
    participant just before that step's thought: some of what they saw came from no action of theirs."""
    lines = []
    for t in trace:
        if "error" in t:
            continue
        o = t.get("output", {})
        acts = ", ".join(str(r["action"].get("type")) + ("" if r["ok"] else " (failed)") for r in t.get("results", []))
        seen = " ".join(str(e) for e in t.get("events") or [])
        lines.append(
            f"Step {t['step']} on '{t.get('title', '')[:50]}' ({t['url'][:80]}): "
            + (f"the browser had just told you: {seen[:600]} Then you " if seen else "")
            + f"felt {o.get('emotion')} (valence {o.get('valence')}, ease {o.get('ease')}). "
            f"Thought: \"{str(o.get('think_aloud', ''))[:260]}\" Did: {acts}."
        )
    for w in waits:
        lines.append(f"You waited {w['seconds']:.0f} s for the site at step {w['step']}{' (it never finished)' if w.get('timeout') else ''}.")
    issues = []
    for p in pages.values():
        for i in (p.get("review") or {}).get("issues", []) + p.get("later_issues", []):
            if isinstance(i, dict):
                issues.append(f"- [{p.get('review', {}).get('page_name') or p['title'][:40]}] {i.get('title')} (severity {i.get('severity')})")
    if issues:
        lines.append("Problems you noted along the way:\n" + "\n".join(issues[:40]))
    return "\n".join(lines)
