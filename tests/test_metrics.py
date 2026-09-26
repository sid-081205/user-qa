from __future__ import annotations

import pytest

from userqa.evaluation.metrics import (
    age_fit,
    analyse_parts,
    name_fidelity,
    placeholders,
    readability,
    repeated_sentences,
    syllables,
    truncated_ending,
    unexpected_names,
)
from userqa.evaluation.questionnaires import score_sus, score_ueqs


def test_syllable_heuristic():
    assert syllables("cat") == 1
    assert syllables("happy") == 2
    assert syllables("melancholy") >= 3


def test_readability_of_simple_and_ornate_prose():
    simple = readability("The cat sat on the mat. The dog ran.")
    assert simple["words"] == 9 and simple["sentences"] == 2
    assert simple["fk_grade"] == pytest.approx(-2.0, abs=0.1)
    assert simple["flesch_reading_ease"] == pytest.approx(117.7, abs=0.1)
    ornate = readability("The ephemeral luminescence of the crepuscular firmament engendered an inexplicable melancholy.")
    assert ornate["fk_grade"] > 14
    assert "luminescence" in ornate["long_words"]
    assert readability("") == {"words": 0, "sentences": 0}


@pytest.mark.parametrize("grade,age,verdict", [
    (1.0, 5, "appropriate"),
    (3.0, 5, "somewhat difficult for the target age"),
    (10.0, 5, "too difficult for the target age"),
    (None, 5, None),
    (3.0, None, None),
])
def test_age_fit(grade, age, verdict):
    assert age_fit(grade, age) == verdict


def test_placeholders_and_glitches():
    hits = placeholders("Hello {{child_name}}, your [object Object] is undefined. Lorem ipsum.")
    assert {"{{child_name}}", "[object Object]", "undefined", "Lorem ipsum"} <= set(hits)
    assert placeholders("Oliver flew the kite with Grandma.") == []


def test_repeated_sentences_count_only_within_one_artifact():
    s = "Once upon a time there lived a curious child named Mia."
    assert repeated_sentences([s, "Mia went outside to play.", s]) == [s]
    assert repeated_sentences([s, s], artifacts=["web page", "pdf"]) == []
    assert repeated_sentences(["Once upon a time.", "Once upon a time."]) == []


def test_truncated_ending():
    assert truncated_ending("They laughed.\nAnd Oliver would always remember") is True
    assert truncated_ending("The End.") is False
    assert truncated_ending("They laughed and laughed.") is False
    assert truncated_ending("") is False


def test_name_fidelity_finds_near_miss_spellings():
    res = name_fidelity("Maisy ran to see Grandma Maggie. Maisy smiled.", ["Maisie", "Grandma Maggie"])
    assert res["Maisie"] == {"token": "Maisie", "mentions": 0, "near_miss_variants": ["Maisy"]}
    assert res["Grandma Maggie"]["token"] == "Maggie" and res["Grandma Maggie"]["mentions"] == 1


def test_unexpected_names_ignore_sentence_starts_and_known_names():
    assert unexpected_names("Oliver met Bartholomew. Then Bartholomew left with Oliver.", ["Oliver"]) == ["Bartholomew"]


def test_analyse_parts_combines_the_checks():
    parts = [{"part": "Page 1", "text": "Oliver flew his kite on the hill with Grandma Maggie.", "artifact": "/book"},
             {"part": "Page 2", "text": "Then {{companion}} came along and Oliver would always remember", "artifact": "/book"}]
    m = analyse_parts(parts, ["Oliver", "Grandma Maggie"], 5)
    assert m["reading_age_requested"] == 5
    assert m["names"]["Oliver"]["mentions"] == 2
    assert "{{companion}}" in m["placeholders"]
    assert m["truncated_ending"] is True
    assert [p["part"] for p in m["per_part"]] == ["Page 1", "Page 2"]


def test_sus_scoring_and_grades():
    best = score_sus([5, 1] * 5)
    assert best["score"] == 100 and best["grade"] == "A+" and best["inconsistent_pairs"] == 0
    assert score_sus([1, 5] * 5)["score"] == 0
    neutral = score_sus([3] * 10)
    assert neutral["score"] == 50 and neutral["grade"] == "F" and neutral["above_average_68"] is False
    assert score_sus([4, 2] * 5)["score"] == 75 and score_sus([4, 2] * 5)["grade"] == "B"


def test_sus_flags_acquiescence():
    yes_to_all = score_sus([5] * 10)
    assert yes_to_all["score"] == 50
    assert yes_to_all["inconsistent_pairs"] == 5 and yes_to_all["consistency_flag"] is True


def test_sus_rejects_incomplete_answers():
    assert score_sus([4] * 9)["score"] is None
    assert score_sus([4] * 9 + [None])["score"] is None


def test_ueq_s_scoring():
    assert score_ueqs([7] * 4 + [1] * 4) == {"pragmatic": 3.0, "hedonic": -3.0, "overall": 0.0}
    assert score_ueqs([4] * 7)["pragmatic"] is None
