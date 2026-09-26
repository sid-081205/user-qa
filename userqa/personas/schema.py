"""Persona specification.

The schema operationalises persona constructs from the HCI / social-simulation
literature so that simulated users differ in *mechanistic*, theory-backed ways
rather than only in a demographic label:

* Goal-directed personas (Cooper 1999; Pruitt & Grudin 2003): end goals,
  experience goals, context of use, frustrations.
* GenderMag cognitive facets (Burnett et al. 2016): motivation, information
  processing style, computer self-efficacy, attitude toward risk, learning style.
  These are behavioural and predictive of how people approach software, which
  reduces the stereotyping risk of identity-only personas (Cheng et al. 2023;
  Wang et al. 2025).
* Big-Five personality descriptors (John & Srivastava 1999), which LLMs can
  express with measurable fidelity (Serapio-Garcia et al. 2023; Jiang et al. 2024).
* Technology-acceptance attitudes (TAM, Davis 1989; UTAUT2 price value,
  Venkatesh et al. 2012) and privacy segmentation (Westin, see Kumaraguru &
  Cranor 2005).
* First-person backstory conditioning (Moon et al. 2024 "Anthology"; Park et al.
  2024) to increase individuation.
* Perception/device constraints (WAI "Stories of Web Users"; F-pattern skimming,
  Nielsen 2006) that are enforced by the environment, not just described.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Optional

import yaml

FACET_VALUES = {
    "motivation": ("task-focused", "tech-curious"),
    "information_processing": ("comprehensive", "selective"),
    "self_efficacy": ("low", "medium", "high"),
    "risk_attitude": ("risk-averse", "risk-tolerant"),
    "learning_style": ("process-oriented", "tinkering"),
}

ATTENTION_MODES = ("full", "skim", "low_vision")
DEVICES = ("desktop", "mobile", "zoom200")


@dataclass
class CognitiveFacets:
    motivation: str = "task-focused"
    information_processing: str = "comprehensive"
    self_efficacy: str = "medium"
    risk_attitude: str = "risk-averse"
    learning_style: str = "process-oriented"

    def describe(self) -> str:
        d = {
            "motivation": {
                "task-focused": "You use technology to get things done, not for its own sake.",
                "tech-curious": "You enjoy technology for its own sake and like trying new features.",
            },
            "information_processing": {
                "comprehensive": "You gather fairly complete information before acting and read explanations.",
                "selective": "You act on the first promising cue and follow it; you rarely read long text.",
            },
            "self_efficacy": {
                "low": "You are not confident with new software; when something goes wrong you tend to blame yourself.",
                "medium": "You are reasonably comfortable with websites but unfamiliar interfaces slow you down.",
                "high": "You are confident with technology and assume problems are the website's fault.",
            },
            "risk_attitude": {
                "risk-averse": "You avoid clicking things whose consequences are unclear (costs, data sharing, irreversible actions).",
                "risk-tolerant": "You happily click around to see what happens.",
            },
            "learning_style": {
                "process-oriented": "You prefer step-by-step guidance and clear instructions.",
                "tinkering": "You learn by exploring and experimenting.",
            },
        }
        return " ".join(d[k].get(getattr(self, k), "") for k in d)


@dataclass
class Persona:
    id: str
    name: str
    age: int
    tagline: str
    backstory: str  # first-person narrative (Anthology-style)
    occupation: str = ""
    household: str = ""
    locale: str = "en-GB"
    goals: list[str] = field(default_factory=list)  # end goals for this kind of product
    experience_goals: list[str] = field(default_factory=list)  # how they want to feel
    frustrations: list[str] = field(default_factory=list)
    facets: CognitiveFacets = field(default_factory=CognitiveFacets)
    big_five: dict[str, str] = field(default_factory=dict)  # trait -> low/medium/high
    tech_attitudes: dict[str, str] = field(default_factory=dict)  # e.g. privacy_segment, price_sensitivity
    accessibility: list[str] = field(default_factory=list)
    language: dict[str, str] = field(default_factory=dict)  # e.g. {"english": "B1 (intermediate)"}
    device: str = "desktop"
    attention: str = "full"
    patience_steps: int = 6  # consecutive frustrating steps before they would give up
    domain_context: dict[str, Any] = field(default_factory=dict)  # concrete facts they know (family, stories)
    voice: str = ""  # how they speak when thinking aloud
    notes_for_simulation: list[str] = field(default_factory=list)
    baseline: bool = False  # ablation: no persona conditioning beyond task facts

    # ---------------------------------------------------------------- I/O
    @classmethod
    def from_dict(cls, d: dict) -> "Persona":
        d = dict(d)
        facets = d.pop("facets", {}) or {}
        p = cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})
        p.facets = CognitiveFacets(**facets) if isinstance(facets, dict) else facets
        p.validate()
        return p

    @classmethod
    def load(cls, path: Path) -> "Persona":
        return cls.from_dict(yaml.safe_load(Path(path).read_text()))

    def to_dict(self) -> dict:
        return asdict(self)

    def dump(self, path: Path) -> None:
        Path(path).write_text(yaml.safe_dump(self.to_dict(), sort_keys=False, allow_unicode=True))

    def validate(self) -> None:
        for k, allowed in FACET_VALUES.items():
            v = getattr(self.facets, k)
            if v not in allowed:
                raise ValueError(f"persona {self.id}: facet {k}={v!r} not in {allowed}")
        if self.attention not in ATTENTION_MODES:
            raise ValueError(f"persona {self.id}: attention must be one of {ATTENTION_MODES}")
        if self.device not in DEVICES:
            raise ValueError(f"persona {self.id}: device must be one of {DEVICES}")

    # ---------------------------------------------------------- prompting
    def profile_text(self) -> str:
        if self.baseline:
            return (
                "You are a typical adult web user (no further persona details).\n\n"
                "Facts you can use when a website asks:\n"
                + yaml.safe_dump(self.domain_context, sort_keys=False, allow_unicode=True).strip()
            )
        lines = [
            f"Name: {self.name} ({self.age}). {self.tagline}",
            f"Occupation: {self.occupation}" if self.occupation else "",
            f"Household: {self.household}" if self.household else "",
            "",
            "In your own words:",
            self.backstory.strip(),
            "",
            "What you want from a product like this: " + "; ".join(self.goals) if self.goals else "",
            "How you want to feel: " + "; ".join(self.experience_goals) if self.experience_goals else "",
            "Things that typically frustrate you: " + "; ".join(self.frustrations) if self.frustrations else "",
            "",
            "How you approach technology: " + self.facets.describe(),
        ]
        if self.big_five:
            lines.append("Personality: " + ", ".join(f"{v} {k}" for k, v in self.big_five.items()) + ".")
        if self.tech_attitudes:
            lines.append("Attitudes: " + "; ".join(f"{k.replace('_', ' ')}: {v}" for k, v in self.tech_attitudes.items()) + ".")
        if self.language:
            lines.append("Language: " + "; ".join(f"{k}: {v}" for k, v in self.language.items()) + ".")
        if self.accessibility:
            lines.append("Accessibility needs: " + "; ".join(self.accessibility) + ".")
        lines.append(f"Device: {self._device_text()}")
        if self.voice:
            lines.append(f"Your think-aloud voice: {self.voice}")
        if self.domain_context:
            lines.append("")
            lines.append("Facts about your life you can use when a website asks (use them consistently, don't invent others unless needed):")
            lines.append(yaml.safe_dump(self.domain_context, sort_keys=False, allow_unicode=True).strip())
        if self.notes_for_simulation:
            lines.append("")
            lines.append("Behavioural notes: " + " ".join(self.notes_for_simulation))
        return "\n".join(l for l in lines if l is not None)

    def _device_text(self) -> str:
        return {
            "desktop": "a laptop/desktop browser",
            "mobile": "a smartphone (small touch screen)",
            "zoom200": "a desktop browser zoomed to 200% because small text is hard to read",
        }[self.device]

    def short(self) -> str:
        return f"{self.name}, {self.age} — {self.tagline}"


def load_persona(ref: str, library_dir: Optional[Path] = None) -> Persona:
    """Load a persona by library id (e.g. ``grandparent_storykeeper``) or YAML path."""
    p = Path(ref)
    if p.suffix in (".yaml", ".yml") and p.exists():
        return Persona.load(p)
    lib = library_dir or Path(__file__).parent / "library"
    f = lib / f"{ref}.yaml"
    if not f.exists():
        raise FileNotFoundError(f"unknown persona {ref!r}; available: {', '.join(list_personas(lib))}")
    return Persona.load(f)


def list_personas(library_dir: Optional[Path] = None) -> list[str]:
    lib = library_dir or Path(__file__).parent / "library"
    return sorted(f.stem for f in lib.glob("*.yaml"))
