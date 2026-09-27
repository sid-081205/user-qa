from __future__ import annotations

import pytest

from userqa.agent.loop import verify_evidence
from userqa.evaluation.issues import cluster_issues, flatten_issues
from userqa.llm import parse_json_lenient


@pytest.mark.parametrize("text,expected", [
    ('{"a": 1}', {"a": 1}),
    ('```json\n{"a": 1}\n```', {"a": 1}),
    ('Sure! Here it is: {"a": [1, 2,], } Hope this helps.', {"a": [1, 2]}),
    ("{\u201ca\u201d: \u201cb\u201d}", {"a": "b"}),
    ('{"note": "line one\nline two"}', {"note": "line one line two"}),
    ('[{"x": 1}, {"x": 2}] trailing words', [{"x": 1}, {"x": 2}]),
    ('{"s": "a } inside a string", "n": 2}', {"s": "a } inside a string", "n": 2}),
])
def test_parse_json_lenient(text, expected):
    assert parse_json_lenient(text) == expected


def test_parse_json_salvages_a_completion_cut_off_by_the_token_limit():
    cut = '{"parts": [{"part": "Page 1", "reaction": "lovely"}, {"part": "Page 2", "reaction": "too sc'
    assert parse_json_lenient(cut) == {"parts": [{"part": "Page 1", "reaction": "lovely"}, {"part": "Page 2", "reaction": "too sc"}]}
    assert parse_json_lenient('{"a": {"b": [1, 2') == {"a": {"b": [1, 2]}}


def test_parse_json_raises_without_json():
    with pytest.raises(ValueError):
        parse_json_lenient("I could not look at the page.")
    with pytest.raises(ValueError):
        parse_json_lenient(None)


PAGE = "Welcome to StoryHearth\nCreate your story\nDon\u2019t worry \u2013 you can change it later.\nPrice: \u00a34.99"


def test_verify_evidence_accepts_exact_quotes():
    assert verify_evidence('The button says "Create your story" but nothing happens', PAGE) == {"quotes": 1, "found": 1, "verified": True}


def test_verify_evidence_normalises_typographic_quotes_and_dashes():
    assert verify_evidence("It reassures me: \u201cDon't worry - you can change it later\u201d", PAGE)["verified"] is True


def test_verify_evidence_rejects_paraphrases():
    res = verify_evidence('It says "Make your story" and "Create your story"', PAGE)
    assert res == {"quotes": 2, "found": 1, "verified": False}


def test_verify_evidence_without_quotes_is_unverifiable():
    assert verify_evidence("The page is confusing", PAGE) == {"quotes": 0, "verified": None}
    assert verify_evidence('It just says "OK"', PAGE) == {"quotes": 0, "verified": None}


def _issue(title, code, sev, page, evidence=""):
    return {"title": title, "code": code, "severity": sev, "page": page, "evidence": evidence}


def test_cluster_issues_merges_a_site_wide_defect_reported_on_each_page():
    issues = [
        _issue("Footer text is too pale to read", "H4 consistency", 2, "Home"),
        _issue("Footer text too pale to read", "H4", 3, "Pricing"),
        _issue("No progress indicator in the book wizard", "H1 visibility", 3, "Create"),
        _issue("Price only revealed at checkout", "H1", 4, "Checkout"),
    ]
    out = cluster_issues(issues)
    assert len(out) == 3
    assert out[0]["title"] == "Price only revealed at checkout" and out[0]["max_severity"] == 4
    footer = next(c for c in out if "Footer" in c["title"])
    assert footer["occurrences"] == 2 and footer["pages"] == ["Pricing", "Home"]
    assert footer["max_severity"] == 3 and footer["mean_severity"] == 2.5


def test_cluster_issues_keeps_different_problems_in_the_same_family_apart():
    out = cluster_issues([_issue("Password rules are hidden", "H9", 3, "Sign up"), _issue("Error message is in red only", "H9", 3, "Sign up")])
    assert len(out) == 2


def test_flatten_issues_keeps_first_visit_and_later_issues():
    pages = {
        "/create": {"title": "Create", "review": {"page_name": "Book wizard", "issues": [{"title": "Too many fields"}, {"no_title": 1}]},
                    "later_issues": [{"title": "Lost my text on Back"}]},
        "/": {"title": "Home", "review": {}},
    }
    out = flatten_issues(pages)
    assert [(i["title"], i["page"], i["source"]) for i in out] == [("Too many fields", "Book wizard", "first_visit"),
                                                                   ("Lost my text on Back", "Book wizard", "later")]
