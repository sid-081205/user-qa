"""Generate a full, individuated persona from a short user-type description.

Following Moon et al. (2024) and Park et al. (2024) we ask the model for a rich
first-person backstory plus the behavioural facets of :mod:`schema`, and we
explicitly instruct it to avoid caricature (Cheng et al. 2023): the persona must
have individual, even counter-stereotypical, details and the facets must be
justified by the backstory rather than by demographics.
"""
from __future__ import annotations

import re

import yaml

from ..llm import LLMClient
from .schema import ATTENTION_MODES, DEVICES, FACET_VALUES, Persona

_PROMPT = """You design research personas for usability studies.
Create ONE realistic, individuated persona for this user type: "{description}".
The persona will use this kind of website: {site_hint}

Rules (to avoid caricature and stereotype):
- Give them specific, idiosyncratic details (a named family member, a concrete memory, a habit). At least one
  detail should run against the stereotype of the user type.
- Derive the behavioural facets from the backstory, not from age/gender/ethnicity.
- Keep it plausible and ordinary; no melodrama.
- domain_context must contain the concrete facts they would type into forms on such a site (names, ages,
  a memory/story they would tell, a favourite object, a place, an e-mail like firstname.lastname@example.com).

Return ONLY a JSON object with these keys:
id (snake_case), name, age (int), tagline, occupation, household, locale, backstory (first person, 90-160 words),
goals (list), experience_goals (list), frustrations (list),
facets: {{motivation: {motivation}, information_processing: {information_processing}, self_efficacy: {self_efficacy},
         risk_attitude: {risk_attitude}, learning_style: {learning_style}}},
big_five: {{openness, conscientiousness, extraversion, agreeableness, neuroticism: low|medium|high}},
tech_attitudes: {{privacy_segment, price_sensitivity, trust_in_ai}},
accessibility (list, may be empty), language (object), device: one of {devices}, attention: one of {attention},
patience_steps (int 3-9), voice, domain_context (object), notes_for_simulation (list).
"""


def _alts(values) -> str:
    return "|".join(values)


def generate_persona(llm: LLMClient, description: str, site_hint: str = "a consumer website") -> Persona:
    prompt = _PROMPT.format(
        description=description,
        site_hint=site_hint,
        devices=_alts(DEVICES),
        attention=_alts(ATTENTION_MODES),
        **{k: _alts(v) for k, v in FACET_VALUES.items()},
    )
    data, _ = llm.chat_json(
        [{"role": "user", "content": prompt}], purpose="persona_generation", max_tokens=3000, temperature=0.9
    )
    data["id"] = re.sub(r"[^a-z0-9_]+", "_", str(data.get("id") or description).lower()).strip("_")[:40]
    for k, allowed in FACET_VALUES.items():
        v = str((data.get("facets") or {}).get(k, allowed[0])).lower()
        data.setdefault("facets", {})[k] = next((a for a in allowed if a in v or v in a), allowed[0])
    if data.get("device") not in DEVICES:
        data["device"] = "desktop"
    if data.get("attention") not in ATTENTION_MODES:
        data["attention"] = "full"
    data["age"] = int(re.sub(r"\D", "", str(data.get("age", 35))) or 35)
    data["patience_steps"] = int(data.get("patience_steps") or 6)
    for key in ("goals", "experience_goals", "frustrations", "accessibility", "notes_for_simulation"):
        if isinstance(data.get(key), str):
            data[key] = [data[key]]
    for key in ("big_five", "tech_attitudes", "language", "domain_context"):
        if not isinstance(data.get(key), dict):
            data[key] = {}
    return Persona.from_dict(data)


def persona_yaml(p: Persona) -> str:
    return yaml.safe_dump(p.to_dict(), sort_keys=False, allow_unicode=True)
