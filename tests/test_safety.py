from __future__ import annotations

import pytest

from userqa.browser.env import SafetyPolicy


@pytest.mark.parametrize("label", ["Pay now", "Buy now", "Purchase", "Place my order", "Confirm payment", "Subscribe", "Upgrade to Pro",
                                   "Buy more credits", "Top-up credits", "Add a card", "Delete my account"])
def test_money_and_irreversible_actions_are_blocked(label):
    assert "would spend money or be irreversible" in SafetyPolicy().check_click(label)


@pytest.mark.parametrize("label", ["Create storybook", "Log in", "Next", "Regenerate PDF", "Edit image", "Payment history"])
def test_ordinary_controls_are_allowed(label):
    assert SafetyPolicy().check_click(label) is None


def test_a_price_is_a_soft_block_that_a_site_can_lift():
    assert "shows a price" in SafetyPolicy().check_click("Generate book ($1.00 of credit)")
    lifted = SafetyPolicy(allowed_click_patterns=[r"generate book"])
    assert lifted.check_click("Generate book ($1.00 of credit)") is None


def test_hard_blocks_cannot_be_lifted():
    policy = SafetyPolicy(allowed_click_patterns=[r"credits?", r"pay"])
    assert policy.check_click("Buy credits") is not None
    assert policy.check_click("Pay now") is not None


@pytest.mark.parametrize("info", [{"name": "Card number"}, {"autocomplete": "cc-number"}, {"placeholder": "CVC"}, {"name": "Expiry date"},
                                  {"name": "IBAN"}])
def test_payment_fields_are_blocked(info):
    assert SafetyPolicy().check_field(info) is not None


def test_ordinary_fields_are_allowed():
    assert SafetyPolicy().check_field({"name": "Child's first name", "type": "text"}) is None


def test_domain_allow_list_admits_subdomains_and_sign_in_providers():
    policy = SafetyPolicy(allowed_domains=["ourlegacy.family"])
    assert policy.domain_allowed("https://www.ourlegacy.family/storybooks")
    assert policy.domain_allowed("https://clerk.ourlegacy.family/v1/client")
    assert policy.domain_allowed("https://accounts.google.com/o/oauth2")
    assert not policy.domain_allowed("https://example.com/")
    assert not policy.domain_allowed("https://ourlegacy.family.evil.test/")
    assert SafetyPolicy().domain_allowed("https://anything.test/")
