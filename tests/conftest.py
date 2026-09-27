from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "experiments"))

from userqa.llm import BudgetExceeded, LLMUsage, parse_json_lenient  # noqa: E402
from userqa.personas.schema import Persona  # noqa: E402


@pytest.fixture
def persona() -> Persona:
    return Persona.from_dict({
        "id": "test_grandparent",
        "name": "Margaret Ellison",
        "age": 72,
        "tagline": "Retired teacher who wants to pass family stories on",
        "backstory": "I taught primary school for thirty years.",
        "domain_context": {"reading_age": 5, "children_in_story": [{"name": "Oliver"}], "other_characters": [{"name": "Grandma Maggie"}]},
    })


class ScriptedLLM:
    """Stands in for LLMClient: answers each call from a function of (purpose, messages) and records the calls."""

    def __init__(self, respond, images: bool = True, max_calls: int = 50, **_):
        self.respond = respond
        self.images = images
        self.max_calls = max_calls
        self.fallbacks: list[str] = []
        self.usage = LLMUsage()
        self.calls: list[dict] = []

    @property
    def remaining(self) -> int:
        return self.max_calls - self.usage.calls

    def supports_images(self, model=None) -> bool:
        return self.images

    def chat_json(self, messages, *, purpose="generic", **kw):
        if self.usage.calls >= self.max_calls:
            raise BudgetExceeded(f"LLM call budget of {self.max_calls} exhausted")
        self.usage.calls += 1
        self.usage.by_purpose[purpose] = self.usage.by_purpose.get(purpose, 0) + 1
        self.calls.append({"purpose": purpose, "messages": messages})
        out = self.respond(purpose, messages)
        return (parse_json_lenient(out) if isinstance(out, str) else out), {"model": "scripted"}


def prompt_text(messages) -> str:
    """All text of a chat request (system and user turns, including multimodal parts)."""
    bits = []
    for m in messages:
        c = m.get("content")
        if isinstance(c, str):
            bits.append(c)
        elif isinstance(c, list):
            bits += [p.get("text", "") for p in c if p.get("type") == "text"]
    return "\n".join(bits)


def n_images(messages) -> int:
    return sum(1 for m in messages if isinstance(m.get("content"), list) for p in m["content"] if p.get("type") == "image_url")


@pytest.fixture
def scripted_llm():
    return ScriptedLLM


def write_capture(run_dir: Path, n: int, text: str, url: str, label: str = "", image_color=None, source: str = "") -> dict:
    """A capture as BrowserEnv writes it: text.txt plus (optionally) one picture of the output."""
    cdir = run_dir / "artifacts" / f"capture_{n:02d}"
    cdir.mkdir(parents=True, exist_ok=True)
    (cdir / "text.txt").write_text(text)
    cap = {"label": label, "url": url, "text": text, "views": [], "images": [], "dir": str(cdir.relative_to(run_dir))}
    if source:
        cap["source"] = source
    if image_color is not None:
        from PIL import Image, ImageDraw

        im = Image.new("RGB", (240, 180), image_color)
        if isinstance(image_color, tuple) and image_color[0] > 200:
            ImageDraw.Draw(im).ellipse((60, 40, 180, 140), fill=(20, 20, 20))
        p = cdir / "img_00.jpg"
        im.save(p, "JPEG")
        cap["images"] = [{"path": str(p.relative_to(run_dir)), "alt": "", "w": 240, "h": 180}]
    (cdir / "capture.json").write_text(json.dumps({k: v for k, v in cap.items() if k != "text"}))
    return cap
