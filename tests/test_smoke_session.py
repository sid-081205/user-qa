"""End-to-end smoke test: a scripted LLM drives the real browser through a tiny local site.

Covers the whole pipeline without network access or LLM cost: perception, actions, the safety policy,
input recording, output capture, output assessment, questionnaires, fidelity audit, summary and report.
"""
from __future__ import annotations

import functools
import http.server
import json
import re
import threading

import pytest

from conftest import ScriptedLLM, n_images, prompt_text
from userqa import runner
from userqa.personas.schema import load_persona

INDEX = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Tiny Tales</title></head><body>
<h1>Tiny Tales</h1><p>Make a one-page story for your child.</p>
<label for="hero">Child's first name</label> <input id="hero" type="text">
<button id="go" onclick="location.href='story.html?name='+encodeURIComponent(document.getElementById('hero').value)">Make my story</button>
<p><button onclick="alert('Checkout')">Buy the printed book (£4.99)</button></p>
</body></html>"""
STORY = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Your story</title></head><body>
<h1>Your story</h1><p id="s"></p>
<script>const n = new URLSearchParams(location.search).get('name') || 'friend';
document.getElementById('s').innerText = 'Once upon a time, ' + n + ' found a blue kite on the hill behind the house. '
  + 'The wind carried it high above the trees, and ' + n + ' laughed all the way home.';</script>
</body></html>"""


@pytest.fixture
def tiny_site(tmp_path):
    root = tmp_path / "site"
    root.mkdir()
    (root / "index.html").write_text(INDEX)
    (root / "story.html").write_text(STORY)

    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a):
            pass

    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(Quiet, directory=str(root)))
    threading.Thread(target=server.serve_forever, daemon=True).start()
    yield f"http://127.0.0.1:{server.server_address[1]}/index.html"
    server.shutdown()


@pytest.fixture
def browser_available(tmp_path):
    from userqa.browser.env import BrowserEnv

    env = BrowserEnv(run_dir=tmp_path, headless=True)
    try:
        env.start()
    except Exception as e:  # pragma: no cover - depends on the machine
        pytest.skip(f"no browser available: {e}")
    finally:
        env.close()


def responder():
    state = {"tried_buy": False}

    def respond(purpose, messages):
        text = prompt_text(messages)
        if purpose == "step":
            if "found a blue kite" in text:
                return {"observation": "My story is here.", "think_aloud": "Oh lovely, it used Oliver's name!", "emotion": "delighted", "valence": 2,
                        "page_review": {"page_name": "Your story", "issues": [
                            {"title": "The story is very short", "code": "OUTPUT", "severity": 1, "evidence": '"The wind carried it high above the trees"'}]},
                        "output_present": True, "output_reaction": "Sweet, but over in two sentences.",
                        "actions": [{"type": "done", "summary": "I made a short story about Oliver and a kite."}]}
            ids = {name: int(i) for i, name in re.findall(r'\[(\d+)\] \w+ "([^"]+)"', text)}
            if not state["tried_buy"]:
                state["tried_buy"] = True
                return {"observation": "A page to make a story.", "think_aloud": "I'd love it printed, let me see the price.", "emotion": "curious",
                        "valence": 1, "site_model": {"what_it_is": "a story maker for children"},
                        "page_review": {"page_name": "Tiny Tales home", "issues": [
                            {"title": "No example of a finished story", "code": "H10", "severity": 2,
                             "evidence": 'It only says "Make a one-page story for your child"'}]},
                        "actions": [{"type": "click", "id": ids["Buy the printed book (£4.99)"]}]}
            return {"observation": "Back to making the story.", "think_aloud": "Fine, I'll just make the story.", "emotion": "neutral", "valence": 0,
                    "actions": [{"type": "type", "id": ids["Child's first name"], "text": "Oliver"}, {"type": "click", "id": ids["Make my story"]}]}
        if purpose == "output_assessment":
            return {"artifact_type": "short story", "overall_reaction": "Sweet but thin.", "keepsake_worthiness": 2,
                    "criteria": {"fidelity": {"score": 4, "why": "uses Oliver"}}, "top_changes": ["Make it longer"],
                    "parts": [{"part": "Story", "reaction": "Nice start.", "problems": [], "suggested_change": "Add Grandma Maggie"}]}
        if purpose == "debrief":
            return {"sus": [{"item": i + 1, "reason": "ok", "rating": 4 if i % 2 == 0 else 2} for i in range(10)],
                    "ueq_s": [{"pair": "x/y", "rating": 5} for _ in range(8)], "nps": 7, "interview": {"purpose": "stories for children"},
                    "recommendations": [{"change": "Show a sample story", "page": "home", "why": "to know what I get", "priority": "high"}],
                    "one_line_verdict": "Nice idea, very short."}
        if purpose == "fidelity_audit":
            return {"voice_consistency": {"score": 4}, "individuation": {"score": 3}, "caricature": {"score": 1}, "knowledge_leakage": {"score": 1},
                    "realism_overall": {"score": 4}}
        raise AssertionError(f"unexpected LLM call: {purpose}")

    return respond


def test_scripted_session_end_to_end(tmp_path, tiny_site, browser_available, monkeypatch):
    llms: list[ScriptedLLM] = []

    def fake_client(**kw):
        llms.append(ScriptedLLM(responder(), **{k: v for k, v in kw.items() if k == "max_calls"}))
        return llms[-1]

    monkeypatch.setattr(runner, "LLMClient", fake_client)
    site = {"name": "tiny tales", "url": tiny_site, "goal": "Make a story for your grandson Oliver and say what you think of it.", "max_steps": 6}
    run_dir = runner.run_session(site, load_persona("grandparent_storykeeper"), tmp_path / "runs", headless=True, log=lambda *a: None)

    llm = llms[0]
    assert [c["purpose"] for c in llm.calls] == ["step", "step", "step", "output_assessment", "debrief", "fidelity_audit"]
    assert n_images(llm.calls[0]["messages"]) == 1
    assert "FAILED - blocked by safety policy (would spend money or be irreversible" in prompt_text(llm.calls[1]["messages"])
    assert 'Child\'s first name (step 2): "Oliver"' in prompt_text(llm.calls[3]["messages"])

    session = json.loads((run_dir / "session.json").read_text())
    assert session["status"] == "done" and session["steps"] == 3
    [entry] = session["inputs"]
    assert {k: entry[k] for k in ("field", "action", "value", "step")} == {"field": "Child's first name", "action": "type", "value": "Oliver", "step": 2}
    assert isinstance(entry["id"], int) and entry["page"].startswith("127.0.0.1:")
    assert len(session["captures"]) == 1
    assert "Oliver found a blue kite" in (run_dir / session["captures"][0]["dir"] / "text.txt").read_text()

    summary = json.loads((run_dir / "summary.json").read_text())
    assert summary["issues"] == 2 and summary["evidence_quotes_verified"] == 1.0
    assert summary["sus"] == 75.0 and summary["nps"] == 7 and summary["keepsake_worthiness"] == 2
    assert summary["fidelity"]["realism_overall"] == 4
    for name in ("trace.jsonl", "output_assessment.json", "debrief.json", "fidelity.json", "report.html", "persona.yaml", "config.json"):
        assert (run_dir / name).exists(), name
