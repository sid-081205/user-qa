from __future__ import annotations

import json
import sys
import threading
import urllib.request
from http.server import ThreadingHTTPServer

import pytest

from userqa.ui import server

PROFILES = [
    {"id": "open_explore", "name": "open-explore", "url": "https://ourlegacy.family/"},
    {"id": "ourlegacy", "name": "ourlegacy", "url": "https://ourlegacy.family/"},
    {"id": "storyhearth", "name": "storyhearth", "url": "http://127.0.0.1:8765/"},
]


def test_a_url_on_a_known_host_picks_that_sites_profile():
    assert server.match_profile("https://www.ourlegacy.family/storybooks", PROFILES) == "ourlegacy"
    assert server.match_profile("http://127.0.0.1:8765/login", PROFILES) == "storyhearth"
    assert server.match_profile("https://example.com", PROFILES) is None
    assert server.match_profile("", PROFILES) is None


def test_the_session_command_carries_the_url_persona_and_goal(tmp_path):
    cmd = server.build_command({"url": "ourlegacy.family", "profile": "ourlegacy", "persona_type": "a techy dad", "goal": "Make a book",
                                "max_steps": 500}, tmp_path)
    assert cmd[:4] == [sys.executable, "-m", "userqa", "run"]
    assert cmd[cmd.index("--site") + 1] == "ourlegacy"
    assert cmd[cmd.index("--url") + 1] == "https://ourlegacy.family"
    assert cmd[cmd.index("--persona-type") + 1] == "a techy dad"
    assert cmd[cmd.index("--goal") + 1] == "Make a book"
    assert cmd[cmd.index("--max-steps") + 1] == "80"
    assert "--headless" not in cmd
    assert "--persona" not in cmd
    assert cmd[-2:] == ["--out", str(tmp_path)]
    with pytest.raises(ValueError):
        server.build_command({}, tmp_path)
    with pytest.raises(ValueError):
        server.build_command({"url": "https://x.test", "persona": "no_such_persona"}, tmp_path)


def _run(d, steps: int = 2, partial: bool = False):
    d.mkdir(parents=True)
    (d / "persona.yaml").write_text("id: dad\nname: Sam\nage: 41\ntagline: a techy dad\n")
    (d / "config.json").write_text(json.dumps({"site": {"name": "demo", "url": "http://x.test/"}, "persona": "dad", "started_utc": "20260101-000000"}))
    lines = [json.dumps({"step": i, "url": "http://x.test/", "screenshot": f"screenshots/step_{i:02d}.jpg", "page_text": "x" * 500,
                         "a11y": [1], "output": {"think_aloud": f"thought {i}"}}) for i in range(1, steps + 1)]
    text = "\n".join(lines) + "\n" + ('{"step": 99, "out' if partial else "")
    (d / "trace.jsonl").write_text(text)
    (d / "screenshots").mkdir()
    (d / "screenshots" / "step_01.jpg").write_bytes(b"\xff\xd8jpeg")
    return d


def test_live_state_follows_the_run_folder_as_it_fills(tmp_path):
    d = _run(tmp_path / "r", steps=3, partial=True)
    st = server.run_state(d)
    assert st["phase"] == "browsing"
    assert [s["step"] for s in st["steps"]] == [1, 2, 3]
    assert "page_text" not in st["steps"][0] and "a11y" not in st["steps"][0]
    assert [s["step"] for s in server.run_state(d, since=2)["steps"]] == [3]
    assert st["persona"]["name"] == "Sam"
    for name, phase in [("session.json", "critiquing"), ("output_assessment.json", "questionnaire"), ("debrief.json", "auditing"),
                        ("summary.json", "done")]:
        (d / name).write_text(json.dumps({"status": "done"}))
        assert server.phase_of(d) == phase
    assert server.phase_of(None) == "preparing"


def test_media_is_limited_to_pictures_inside_the_run(tmp_path, monkeypatch):
    runs = tmp_path / "runs"
    d = _run(runs / "ui" / "r")
    (tmp_path / "secret.jpg").write_bytes(b"x")
    (d / "notes.txt").write_text("x")
    monkeypatch.setattr(server, "RUNS_ROOT", runs)
    assert server.resolve_run("ui/r") == d.resolve()
    assert server.resolve_run("../") is None
    assert server.resolve_media(d, "screenshots/step_01.jpg") == (d / "screenshots" / "step_01.jpg").resolve()
    assert server.resolve_media(d, "../../../secret.jpg") is None
    assert server.resolve_media(d, "notes.txt") is None
    assert server.resolve_media(d, "screenshots/missing.jpg") is None


def test_the_http_api_serves_the_page_the_run_list_and_a_runs_state(tmp_path, monkeypatch):
    runs = tmp_path / "runs"
    _run(runs / "live" / "r1")
    _run(runs / "ui" / "job1" / "r2")
    (runs / "ui" / "job1" / "r2" / "summary.json").write_text(json.dumps({"status": "done", "steps": 2}))
    monkeypatch.setattr(server, "RUNS_ROOT", runs)
    httpd = ThreadingHTTPServer(("127.0.0.1", 0), server.make_handler(server.App()))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{httpd.server_address[1]}"
    try:
        page = urllib.request.urlopen(base + "/").read().decode()
        assert "Start session" in page
        listed = json.loads(urllib.request.urlopen(base + "/api/runs").read())
        assert {r["run"]: (r["folder"], r["status"]) for r in listed} == {"live/r1": ("live", "incomplete"), "ui/job1/r2": ("ui", "done")}
        st = json.loads(urllib.request.urlopen(base + "/api/state?run=live/r1&since=1").read())
        assert st["phase"] == "incomplete" and [s["step"] for s in st["steps"]] == [2]
        assert urllib.request.urlopen(base + "/media?run=live/r1&path=screenshots/step_01.jpg").read() == b"\xff\xd8jpeg"
        with pytest.raises(urllib.error.HTTPError):
            urllib.request.urlopen(base + "/api/state?run=../..")
    finally:
        httpd.shutdown()
