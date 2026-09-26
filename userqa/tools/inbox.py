"""Disposable e-mail inbox used by simulated users to receive sign-up / login codes.

Real users verify their e-mail address by opening their mailbox.  To let a
simulated user do the same on a real website (e.g. passwordless "email code"
logins such as Clerk), we give every persona a real, disposable mailbox from
the free mail.tm API.  The persona can then call the ``read_inbox`` action.
"""
from __future__ import annotations

import json
import re
import secrets
import string
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional

import requests

API = "https://api.mail.tm"
_CODE_RE = re.compile(r"(?<![\d#])(\d{6})(?!\d)")


@dataclass
class Mailbox:
    address: str
    password: str
    token: str = ""

    def to_json(self) -> dict:
        return asdict(self)


class Inbox:
    """Thin client over the mail.tm REST API."""

    def __init__(self, mailbox: Mailbox, timeout: float = 20.0):
        self.mailbox = mailbox
        self.timeout = timeout
        self._seen: set[str] = set()
        if not mailbox.token:
            self._login()

    # ------------------------------------------------------------------ setup
    @classmethod
    def create(cls, prefix: str = "userqa") -> "Inbox":
        domains = requests.get(f"{API}/domains", timeout=20).json()["hydra:member"]
        domain = next(d["domain"] for d in domains if d.get("isActive"))
        password = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(20))
        for attempt in range(4):
            # mail.tm rejects some usernames (e.g. containing blocklisted words); fall back to a neutral prefix.
            local = f"{prefix if attempt == 0 else 'qa'}{secrets.token_hex(4)}".lower()
            r = requests.post(f"{API}/accounts", json={"address": f"{local}@{domain}", "password": password}, timeout=20)
            if r.status_code in (422, 429) and attempt < 3:  # address taken or rate-limited: retry with a new address
                time.sleep(2 + 3 * attempt)
                continue
            r.raise_for_status()
            break
        # mail.tm normalises the local part, so the canonical address is the one it returns.
        return cls(Mailbox(address=r.json()["address"], password=password))

    @classmethod
    def load_or_create(cls, path: Path, prefix: str = "userqa") -> "Inbox":
        path = Path(path)
        if path.exists():
            box = Mailbox(**json.loads(path.read_text()))
            try:
                return cls(box)
            except Exception:
                pass
        inbox = cls.create(prefix)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(inbox.mailbox.to_json(), indent=2))
        return inbox

    def _login(self, attempts: int = 4) -> None:
        for i in range(attempts):
            r = requests.post(
                f"{API}/token",
                json={"address": self.mailbox.address, "password": self.mailbox.password},
                timeout=self.timeout,
            )
            if r.ok:
                self.mailbox.token = r.json()["token"]
                return
            time.sleep(2 * (i + 1))
        r.raise_for_status()

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self.mailbox.token}"}

    # --------------------------------------------------------------- reading
    def list_messages(self) -> list[dict]:
        r = requests.get(f"{API}/messages", headers=self._headers(), timeout=self.timeout)
        if r.status_code == 401:
            self._login()
            r = requests.get(f"{API}/messages", headers=self._headers(), timeout=self.timeout)
        r.raise_for_status()
        return r.json().get("hydra:member", [])

    def get_message(self, msg_id: str) -> dict:
        r = requests.get(f"{API}/messages/{msg_id}", headers=self._headers(), timeout=self.timeout)
        r.raise_for_status()
        return r.json()

    def mark_all_seen(self) -> None:
        for m in self.list_messages():
            self._seen.add(m["id"])

    def wait_for_message(self, timeout: float = 90.0, poll: float = 4.0, only_new: bool = True) -> Optional[dict]:
        """Block until a (new) message arrives; return a compact dict or ``None``."""
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                msgs = self.list_messages()
            except requests.RequestException:
                msgs = []
            fresh = [m for m in msgs if not (only_new and m["id"] in self._seen)]
            if fresh:
                newest = sorted(fresh, key=lambda m: m.get("createdAt", ""), reverse=True)[0]
                self._seen.add(newest["id"])
                full = self.get_message(newest["id"])
                text = full.get("text") or re.sub(r"<[^>]+>", " ", " ".join(full.get("html") or []))
                text = re.sub(r"\s+", " ", text).strip()
                subject = full.get("subject", "")
                code = _extract_code(subject + " " + text)
                return {
                    "from": (full.get("from") or {}).get("address", ""),
                    "subject": subject,
                    "text": text[:1500],
                    "code": code,
                }
            time.sleep(poll)
        return None


def _extract_code(text: str) -> Optional[str]:
    m = _CODE_RE.search(text)
    return m.group(1) if m else None
