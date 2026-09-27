"""Episodic memory for a persona session (after Park et al. 2023's memory stream).

Recent steps are replayed verbatim; older ones are compressed to one line so the
prompt stays small while the persona keeps a coherent sense of its journey.
Explicit ``memory_note``s (e.g. a price seen earlier, a code) are always kept.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class StepMemory:
    step: int
    page: str
    thought: str
    emotion: str
    actions: list[str]
    outcome: str


@dataclass
class Memory:
    recent_window: int = 8
    steps: list[StepMemory] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def add(self, m: StepMemory) -> None:
        self.steps.append(m)

    def note(self, text: str) -> None:
        text = (text or "").strip()
        if text and text not in self.notes:
            self.notes.append(text[:200])
            self.notes = self.notes[-15:]

    def journey_text(self) -> str:
        if not self.steps:
            return "(this is the start of your session)"
        old = self.steps[: -self.recent_window]
        recent = self.steps[-self.recent_window :]
        lines = []
        for s in old:
            lines.append(f"S{s.step} [{s.page}] {'; '.join(s.actions)[:140]} -> {s.outcome[:80]}")
        for s in recent:
            lines.append(
                f"S{s.step} [{s.page}] (felt {s.emotion}) you thought: \"{s.thought[:220]}\"\n"
                f"    you did: {'; '.join(s.actions)[:300]}\n    result: {s.outcome[:220]}"
            )
        return "\n".join(lines)

    def notes_text(self) -> str:
        if not self.notes:
            return ""
        return "=== NOTES YOU MADE ===\n" + "\n".join(f"- {n}" for n in self.notes)
