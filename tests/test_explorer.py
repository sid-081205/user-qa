from __future__ import annotations

import json

from userqa.report.explorer import build_explorer


def _write_run(d, persona_id: str, name: str) -> None:
    d.mkdir(parents=True)
    (d / "persona.yaml").write_text(f"id: {persona_id}\nname: {name}\ntagline: a test persona\n")
    (d / "config.json").write_text(json.dumps({"site": {"name": "demo", "url": "http://x.test/", "goal": "Make a book for Oliver."}, "persona": persona_id}))
    step = {"step": 1, "url": "http://x.test/", "title": "Home", "new_page": True, "screenshot": "screenshots/step_01.jpg",
            "output": {"think_aloud": "Where do I start?", "valence": 1, "page_review": {"page_name": "Home", "first_impression": f"{name} likes it"}},
            "results": [{"action": {"type": "click", "id": 3}, "ok": True, "message": "clicked"}]}
    (d / "trace.jsonl").write_text(json.dumps(step) + "\n")
    call = {"purpose": "step", "model": "m", "request": [{"role": "system", "content": "You role-play <Margaret>."},
                                                        {"role": "user", "content": [{"type": "text", "text": "Page 1"},
                                                                                     {"type": "image_url", "image_url": "<image sha1=0>"}]}],
            "response": json.dumps({"think_aloud": "Where do I start?"}), "usage": {"prompt_tokens": 10, "completion_tokens": 5}}
    (d / "llm_calls.jsonl").write_text(json.dumps(call) + "\n")
    (d / "session.json").write_text(json.dumps({
        "status": "done", "inputs": [{"field": "Story", "action": "type", "value": "The blue kite"}],
        "pages": {"home": {"url": "http://x.test/", "first_step": 1, "review": {"first_impression": f"{name} likes it"}}},
        "captures": [{"label": "Book", "url": "http://x.test/book", "dir": "artifacts/capture_01", "images": [{"path": "artifacts/capture_01/img_00.jpg", "alt": "Cover"}]}]}))
    (d / "output_assessment.json").write_text(json.dumps({
        "overall_reaction": "Not our family.", "keepsake_worthiness": 2, "top_changes": ["Keep Grandma in the story"],
        "images": [{"ref": "I1", "path": "artifacts/capture_01/img_00.jpg", "desc": "cover"}],
        "parts": [{"part": "Cover", "image_refs": ["I1"], "reaction": "Wrong grandparent", "suggested_change": "Draw Grandma", "rewrite": "Grandma's Kite"}]}))
    (d / "summary.json").write_text(json.dumps({"steps": 1, "sus": 40, "keepsake_worthiness": 2}))


def test_media_copy_is_used_when_the_run_has_no_pictures(tmp_path, monkeypatch):
    from PIL import Image

    from userqa.report import explorer

    runs, media = tmp_path / "runs", tmp_path / "runs_media"
    _write_run(runs / "suite" / "r1", "grandparent", "Margaret")
    shot = runs / "suite" / "r1" / "screenshots" / "step_01.jpg"
    shot.parent.mkdir()
    Image.new("RGB", (1600, 900), "white").save(shot)
    assert explorer.export_media(runs, media, max_px=400) == 1
    shot.unlink()
    monkeypatch.setattr(explorer, "RUNS_ROOT", runs)
    monkeypatch.setattr(explorer, "MEDIA_ROOT", media)
    build_explorer([runs], tmp_path / "site")
    html = (tmp_path / "site" / "runs" / "suite_r1.html").read_text()
    assert "runs_media/suite/r1/screenshots/step_01.jpg" in html
    with Image.open(media / "suite" / "r1" / "screenshots" / "step_01.jpg") as im:
        assert max(im.size) == 400


def test_explorer_shows_prompts_inputs_outputs_and_comparison(tmp_path):
    runs = tmp_path / "runs" / "suite"
    _write_run(runs / "r1", "grandparent", "Margaret")
    _write_run(runs / "r2", "techy", "Daniel")
    index = build_explorer([tmp_path / "runs"], tmp_path / "site")
    assert index.exists()
    pages = sorted((tmp_path / "site" / "runs").glob("*.html"))
    assert len(pages) == 2
    html = pages[0].read_text()
    assert "You role-play &lt;Margaret&gt;." in html
    assert "picture sent to the model" in html
    assert "The blue kite" in html and "Make a book for Oliver." in html
    assert "Wrong grandparent" in html and "Grandma&#x27;s Kite" in html
    assert "Picture not in this copy" in html
    compare = (tmp_path / "site" / "compare.html").read_text()
    assert "Margaret likes it" in compare and "Daniel likes it" in compare
