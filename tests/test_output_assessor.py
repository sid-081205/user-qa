from __future__ import annotations

import json
import re

from conftest import n_images, prompt_text, write_capture
from userqa.evaluation.output_assessor import (
    OutputAssessor,
    _artifact_label,
    _changes_note,
    _compact_parts,
    _inputs_text,
    _merge_parts,
    _part_key,
    _redrawn,
    _supersede,
    expected_names,
    reading_age,
)
from userqa.runner import backfill_input_context

PAGE_1 = "Oliver ran up the green hill with Grandma Maggie on a windy Sunday morning.\nThe blue kite tugged at the string like a puppy that wanted to play."
PAGE_2 = "They sat on the bench and shared warm scones while the kite danced above them.\nGrandma told Oliver how she first flew it when she was a little girl."
PAGE_3 = "When the sun went down they walked home, holding the kite between them.\nOliver promised to keep it safe for his own grandchildren one day."
PAGE_3_FIXED = "When the sun went down they walked home, holding the kite between them.\nOliver promised to look after the kite for the rest of his life."


def test_part_key_matches_scene_and_page_labels():
    assert _part_key("Page 9 (Scene 9)") == _part_key("Scene 9") == "scene 9"
    assert _part_key("Page 3") == "page 3"
    assert _part_key("Front cover!") == "front cover"


def test_merge_parts_folds_a_part_seen_in_two_batches():
    parts = [{"part": "Scene 9", "image_refs": ["I1"], "reaction": "lovely"}]
    new = [{"part": "Page 9 (Scene 9)", "image_refs": ["I5"], "picture_description": "a kite over a hill"}, {"part": "Scene 10"}]
    out = _merge_parts(parts, new)
    assert [p["part"] for p in out] == ["Scene 9", "Scene 10"]
    assert out[0]["image_refs"] == ["I1", "I5"]
    assert out[0]["picture_description"] == "a kite over a hill"
    assert out[0]["reaction"] == "lovely"


def test_changes_note_lists_removed_and_added_lines():
    note = _changes_note("Grandpa's daddy flew the kite on the hill every Sunday.", "My father flew the kite on the hill every Sunday.")
    assert note.startswith('no longer there: "Grandpa\'s daddy')
    assert 'new: "My father flew' in note
    assert _changes_note(PAGE_1, PAGE_1) == "the text did not change"


def test_artifact_labels_name_files_and_pages():
    assert _artifact_label({"url": "file://01_storybook_123.pdf/page-1"}, 32) == 'the file "storybook_123.pdf" (32 pages)'
    assert _artifact_label({"url": "file://02_clip.mp4/frame-1"}, 8) == 'the file "clip.mp4" (8 frames)'
    assert _artifact_label({"url": "https://x.test/book/42", "label": "auto: Your Story"}, 3) == 'the web page /book/42 ("Your Story")'


def test_supersede_drops_an_in_progress_capture_of_the_same_page():
    generating = {"url": "https://x.test/book", "label": "generating"}
    other = {"url": "https://x.test/dashboard", "label": "dashboard"}
    final = {"url": "https://x.test/book", "label": "finished"}
    texts = [PAGE_1, "Your books\nGrandpa's Blue Kite, 10 scenes, created today.", PAGE_1 + "\n" + PAGE_2]
    keep, replaced = _supersede([generating, other, final], texts)
    assert keep == [1, 2]
    assert replaced == {2: [0]}


def test_supersede_keeps_short_captures_and_different_pages():
    caps = [{"url": "https://x.test/book"}, {"url": "https://x.test/book"}]
    keep, _ = _supersede(caps, ["Loading your story now.", "Loading your story now."])
    assert keep == [0, 1]


def test_supersede_drops_pdf_viewer_screenshots_when_the_file_was_captured():
    viewer = {"url": "https://x.test/files/storybook_1.pdf", "label": "PDF viewer"}
    page = {"url": "file://01_storybook_1.pdf/page-1", "source": "file"}
    keep, _ = _supersede([viewer, page], [PAGE_1, PAGE_1])
    assert keep == [1]


def test_supersede_treats_a_regenerated_file_as_a_new_version():
    old = [{"url": f"file://01_book_a.pdf/page-{k}", "source": "file"} for k in (1, 2, 3)]
    new = [{"url": f"file://02_book_b.pdf/page-{k}", "source": "file"} for k in (1, 2, 3)]
    texts = [PAGE_1, PAGE_2, PAGE_3, PAGE_1, PAGE_2, PAGE_3_FIXED]
    keep, replaced = _supersede(old + new, texts)
    assert keep == [3, 4, 5]
    assert replaced == {3: [0], 4: [1], 5: [2]}


def test_supersede_keeps_two_different_files():
    a = [{"url": f"file://01_book_a.pdf/page-{k}", "source": "file"} for k in (1, 2, 3)]
    b = [{"url": f"file://02_other.pdf/page-{k}", "source": "file"} for k in (1, 2, 3)]
    keep, replaced = _supersede(a + b, [PAGE_1, PAGE_2, PAGE_3, "Completely different words appear on this first page now.",
                                        "And another different page with its own long sentence here.", "A third one that shares nothing at all with the book."])
    assert keep == [0, 1, 2, 3, 4, 5]
    assert replaced == {}


def test_redrawn_compares_pictures_by_average_hash(tmp_path):
    plain = write_capture(tmp_path, 1, PAGE_1, "https://x.test/book", image_color=(30, 60, 200))
    same = write_capture(tmp_path, 2, PAGE_1, "https://x.test/book", image_color=(30, 60, 200))
    drawn = write_capture(tmp_path, 3, PAGE_1, "https://x.test/book", image_color=(255, 255, 255))
    assert _redrawn(plain, same, tmp_path) == []
    assert _redrawn(plain, drawn, tmp_path) == [0]


def test_expected_names_from_persona_and_inputs(persona):
    inputs = [{"field": "Child's first name", "value": "Oliver"}, {"field": "Who else is in the story?", "value": "Biscuit the dog"},
              {"field": "Where does the story happen?", "value": "the hill behind the house"}]
    assert expected_names(persona, inputs) == ["Oliver", "Grandma Maggie", "Biscuit the dog"]


def test_reading_age_ignores_the_storytellers_age(persona):
    assert reading_age(persona, [{"field": "Age", "value": "6"}]) == 6.0
    assert reading_age(persona, [{"field": "Reading age", "value": 7}]) == 7.0
    assert reading_age(persona, [{"field": "Age", "value": "4"}, {"field": "Age", "value": "6"}]) == 6.0
    persona.domain_context["reading_age"] = 8
    assert reading_age(persona, [{"field": "Teller’s age", "value": "5"}, {"field": "Page", "value": "3"}]) == 8.0
    assert reading_age(persona, [{"field": "Your age", "value": "72"}]) == 8.0


def test_inputs_text_marks_cleared_and_replaced_entries():
    create = "site.test/create | Create"
    txt = _inputs_text([
        {"field": "Character description", "value": "Oliver, age 5", "step": 9, "page": create, "id": 66},
        {"field": "Character description", "value": "Grandma Maggie, my grandmother", "step": 10, "page": create, "id": 70},
        {"field": "Character description", "value": "Grandma Maggie, Oliver's grandmother", "step": 11, "page": create, "id": 70},
        {"field": "Teller’s age", "value": None, "step": 12, "page": create, "id": 80},
    ])
    lines = txt.splitlines()
    assert lines[0] == '- Character description (step 9): "Oliver, age 5"'
    assert lines[1] == '- Character description (step 10): "Grandma Maggie, my grandmother"  [you changed this field later; only your last entry counts]'
    assert lines[2] == '- Character description (step 11): "Grandma Maggie, Oliver\'s grandmother"'
    assert lines[3] == "- Teller’s age (step 12): (you cleared this field)"
    assert "a field with the same name on another scene or page is a different field" in lines[4]


def test_inputs_text_never_merges_same_named_fields_without_element_ids():
    txt = _inputs_text([{"field": "Narrative Text", "value": "Scene 1 text"}, {"field": "Narrative Text", "value": "Scene 2 text"}])
    assert "changed this field later" not in txt
    assert txt.splitlines()[:2] == ['- Narrative Text: "Scene 1 text"', '- Narrative Text: "Scene 2 text"']
    assert "truncated" not in _inputs_text([{"field": "Idea", "value": "x" * 10}])
    assert "cut this to 200" in _inputs_text([{"field": "Idea", "value": "x" * 10, "truncated_to": 200}])


def test_backfill_recovers_step_screen_and_element_from_the_trace():
    trace = [
        {"step": 1, "page_key": "a | Home", "results": [{"action": {"type": "click", "id": 3}, "ok": True}]},
        {"step": 2, "error": "timeout"},
        {"step": 3, "page_key": "a/create | Create", "results": [{"action": {"type": "type", "id": 24, "text": "One summer"}, "ok": True},
                                                                  {"action": {"type": "type", "id": 25, "text": "x"}, "ok": False},
                                                                  {"action": {"type": "set_range", "id": 30, "value": 5}, "ok": True}]},
    ]
    inputs = [{"field": "Story", "action": "type", "value": "One summer"}, {"field": "Watercolor", "action": "choose", "value": "watercolor"},
              {"field": "Reading age", "action": "set_range", "value": 5}]
    backfill_input_context(inputs, trace)
    assert [(i.get("step"), i.get("page"), i.get("id")) for i in inputs] == [(3, "a/create | Create", 24), (None, None, None), (3, "a/create | Create", 30)]
    mismatched = [{"field": "Story", "action": "type", "value": "One summer"}]
    assert backfill_input_context(mismatched, trace + trace) == [{"field": "Story", "action": "type", "value": "One summer"}]


def test_compact_parts_keeps_the_review_and_drops_verbatim_text():
    parts = [{"part": "Page 1", "text": "long verbatim text " * 50, "reaction": "sweet", "artifact": "the web page /book",
              "problems": [{"criterion": "fidelity", "severity": 3, "evidence": "the hero is called Oscar", "extra": 1}], "suggested_change": "use Oliver"}, "junk"]
    out = _compact_parts(parts)
    assert out == [{"output": "the web page /book", "part": "Page 1", "reaction": "sweet",
                    "problems": [{"criterion": "fidelity", "severity": 3, "evidence": "the hero is called Oscar"}], "suggested_change": "use Oliver"}]


def _page_text(k: int, hero: str = "Oliver") -> str:
    return f"Page {k}\nOn page {k} {hero} and Grandma Maggie flew the blue kite over hill number {k}.\nThe wind carried it {k} times around the old oak tree."


def _book(tmp_path, n_pages: int, url: str = "https://x.test/book"):
    return [write_capture(tmp_path, k + 1, _page_text(k + 1), url, label=f"Page {k + 1}", image_color=(255, 255, 255)) for k in range(n_pages)]


def _pdf(tmp_path, n_pages: int):
    return [write_capture(tmp_path, 50 + k, _page_text(k + 1, hero="Olly"), f"file://01_storybook.pdf/page-{k + 1}",
                          label=f"storybook.pdf page {k + 1} of {n_pages}", image_color=(255, 255, 255), source="file") for k in range(n_pages)]


def _judge_reply(purpose, messages):
    """Reviews exactly the pictures it is shown, naming each part after the page its capture shows."""
    if purpose == "output_synthesis":
        return {"overall_reaction": "Mixed.", "criteria": {"fidelity": {"score": 2}}, "top_changes": ["Fix the names"], "keepsake_worthiness": 2}
    text = prompt_text(messages)
    labels = {}
    for label, pics in re.findall(r'\[Capture \d+: "([^"]*)" - [^\n]*\]\ntext:\n.*?\npictures in this capture: ([^\n]*)', text, re.S):
        for ref in re.findall(r"I\d+", pics):
            labels[ref] = label
    shown = re.search(r"You are now looking at pictures ([I\d, ]+) of it", text)
    refs = re.findall(r"I\d+", shown.group(1)) if shown else list(labels)
    parts = [{"part": "Page " + re.search(r"page (\d+)", labels[r], re.I).group(1), "reaction": "fine", "image_refs": [r], "problems": []} for r in refs]
    return json.dumps({"artifact_type": "picture book", "overall_reaction": "Mixed.", "keepsake_worthiness": 2, "parts": parts})


def test_assess_reviews_a_small_output_in_one_call(tmp_path, persona, scripted_llm):
    llm = scripted_llm(_judge_reply)
    res = OutputAssessor(llm, tmp_path).assess(persona, [{"field": "Age", "value": "5"}], _book(tmp_path, 3), [])
    assert [c["purpose"] for c in llm.calls] == ["output_assessment"]
    assert n_images(llm.calls[0]["messages"]) == 3
    assert [p["part"] for p in res["parts"]] == ["Page 1", "Page 2", "Page 3"]
    assert res["reading_age"] == 5.0
    assert [im["ref"] for im in res["images"]] == ["I1", "I2", "I3"]


def test_assess_batches_a_long_output_and_synthesises_once(tmp_path, persona, scripted_llm):
    llm = scripted_llm(_judge_reply)
    res = OutputAssessor(llm, tmp_path, max_images_per_call=4).assess(persona, [], _book(tmp_path, 10), [])
    assert [c["purpose"] for c in llm.calls] == ["output_assessment"] * 3 + ["output_synthesis"]
    assert [n_images(c["messages"]) for c in llm.calls[:3]] == [4, 4, 2]
    second = prompt_text(llm.calls[1]["messages"])
    assert "This is output 1 of 1" in second
    assert "ALREADY reviewed these parts of it - do not review them again: Page 1; Page 2; Page 3; Page 4." in second
    assert [p["part"] for p in res["parts"]] == [f"Page {k}" for k in range(1, 11)]
    assert res["top_changes"] == ["Fix the names"]


def test_assess_keeps_pages_of_different_outputs_apart(tmp_path, persona, scripted_llm):
    llm = scripted_llm(_judge_reply)
    res = OutputAssessor(llm, tmp_path, max_images_per_call=4).assess(persona, [], _book(tmp_path, 3) + _pdf(tmp_path, 3), [])
    assert [c["purpose"] for c in llm.calls] == ["output_assessment", "output_assessment", "output_synthesis"]
    assert 'This is output 2 of 2: the file "storybook.pdf" (3 pages)' in prompt_text(llm.calls[1]["messages"])
    assert [(p["artifact"], p["part"]) for p in res["parts"]] == [
        ('the web page /book ("Page 1")', "Page 1"), ('the web page /book ("Page 1")', "Page 2"), ('the web page /book ("Page 1")', "Page 3"),
        ('the file "storybook.pdf" (3 pages)', "Page 1"), ('the file "storybook.pdf" (3 pages)', "Page 2"), ('the file "storybook.pdf" (3 pages)', "Page 3"),
    ]


def test_assess_without_vision_sends_no_pictures(tmp_path, persona, scripted_llm):
    llm = scripted_llm(_judge_reply)
    caps = _book(tmp_path, 2)
    caps[0]["images"][0]["alt"] = "Oliver and his grandmother flying a kite"
    OutputAssessor(llm, tmp_path, vision=False).assess(persona, [], caps, [])
    msgs = llm.calls[0]["messages"]
    assert n_images(msgs) == 0
    assert "their alt text says: Oliver and his grandmother flying a kite" in prompt_text(msgs)


def test_assess_tells_the_judge_what_changed_in_a_revised_page(tmp_path, persona, scripted_llm):
    llm = scripted_llm(_judge_reply)
    first = write_capture(tmp_path, 1, "\n".join(["Page 3", PAGE_1, PAGE_2, PAGE_3]), "https://x.test/book", label="Page 3 (first draft)",
                          image_color=(30, 60, 200))
    final = write_capture(tmp_path, 2, "\n".join(["Page 3", PAGE_1, PAGE_2, PAGE_3_FIXED]), "https://x.test/book", label="Page 3",
                          image_color=(255, 255, 255))
    res = OutputAssessor(llm, tmp_path).assess(persona, [], [first, final], [])
    text = prompt_text(llm.calls[0]["messages"])
    assert 'compared with the first version you saw ("Page 3 (first draft)")' in text
    assert 'no longer there: "Oliver promised to keep it safe' in text
    assert "pictures redrawn since then: I1" in text
    assert res["superseded_captures"] == ["Page 3 (first draft)"]
    assert res["version_changes"][0]["part"] == "Page 3"
    assert n_images(llm.calls[0]["messages"]) == 1


def test_assess_tells_the_judge_which_wording_came_from_the_users_own_inputs(tmp_path, persona, scripted_llm):
    llm = scripted_llm(_judge_reply)
    story = "I help him fly Grandpa's blue kite on the windy hill."
    page = write_capture(tmp_path, 1, "Page 1\nOliver and Grandpa fly Grandpa's blue kite together.\nThe kite climbs above the farmhouse.",
                         "https://x.test/book", label="Page 1", image_color=(255, 255, 255))
    res = OutputAssessor(llm, tmp_path).assess(persona, [{"field": "Story Narrative", "action": "type", "value": story}], [page], [])
    text = prompt_text(llm.calls[0]["messages"])
    assert "Wording the output repeats from your own inputs (this came from you, not from the website): \"fly grandpa's blue kite\"" in text
    assert "check your own inputs below" in text
    assert res["measurements"]["phrases_from_inputs"] == ["fly grandpa's blue kite"]


def test_assess_without_captures_is_skipped(tmp_path, persona, scripted_llm):
    llm = scripted_llm(_judge_reply)
    assert OutputAssessor(llm, tmp_path).assess(persona, [], [], [])["skipped"] is True
    assert llm.calls == []
