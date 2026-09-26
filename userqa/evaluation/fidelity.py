"""Persona-fidelity audit of a simulated session.

A separate judge call rates whether behaviour and verbalisations were consistent
with the persona's specified facets, whether the simulation drifted into
caricature (exaggerated, stereotyped traits; cf. CoMPosT, Cheng et al. 2023), and
whether the "participant" used knowledge the person would not have (the
hyper-accuracy distortion noted by Aher et al. 2023).
"""
from __future__ import annotations

from ..llm import LLMClient, LLMError
from ..personas.schema import Persona

TEMPLATE = """You are an experienced qualitative UX researcher auditing a SIMULATED usability-study participant (an AI role-playing a persona). Judge the simulation, not the website.

=== PERSONA SPECIFICATION ===
{profile}

Specified cognitive facets (GenderMag): {facets}

=== SESSION TRANSCRIPT (think-aloud and actions) ===
{journey}

Rate each item 1-5 with a short justification citing steps:
- facet_consistency: for each facet, did behaviour match the specification? (e.g. a risk-averse person hesitating before unclear actions; a selective processor acting on first cues; low self-efficacy blaming themselves)
- voice_consistency: did the think-aloud sound like this person throughout?
- individuation: did the participant come across as a specific individual (5) rather than a generic user (1)?
- caricature: 1 = natural, 5 = exaggerated/stereotyped portrayal of the persona's group
- knowledge_leakage: 1 = none, 5 = frequently used knowledge/skills this person would not have (developer jargon, guessing hidden URLs, perfect recall)
- realism_overall: would a real person like this plausibly behave this way?

Return ONLY JSON:
{{"facet_consistency": {{"motivation": {{"score": 1-5, "why": "..."}}, "information_processing": {{...}}, "self_efficacy": {{...}}, "risk_attitude": {{...}}, "learning_style": {{...}}}},
 "voice_consistency": {{"score": 1-5, "why": "..."}}, "individuation": {{"score": 1-5, "why": "..."}},
 "caricature": {{"score": 1-5, "why": "...", "examples": ["..."]}}, "knowledge_leakage": {{"score": 1-5, "examples": ["..."]}},
 "realism_overall": {{"score": 1-5, "why": "..."}}}}"""


def audit_fidelity(llm: LLMClient, persona: Persona, journey: str) -> dict:
    if persona.baseline:
        return {"skipped": True, "reason": "baseline condition has no persona"}
    f = persona.facets
    prompt = TEMPLATE.format(
        profile=persona.profile_text(),
        facets=f"motivation={f.motivation}, information_processing={f.information_processing}, self_efficacy={f.self_efficacy}, risk_attitude={f.risk_attitude}, learning_style={f.learning_style}",
        journey=journey[:30000],
    )
    try:
        data, _ = llm.chat_json([{"role": "user", "content": prompt}], purpose="fidelity_audit", max_tokens=4000, temperature=0.0)
        return data if isinstance(data, dict) else {"error": "bad format"}
    except LLMError as e:
        return {"error": str(e)}
