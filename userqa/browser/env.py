"""Playwright browser environment for persona agents.

The environment exposes a WebArena-style observation (numbered interactive
elements in reading order) plus an optional screenshot, and a small, safe action
space.  Perception is persona-conditioned: device profile (desktop / phone /
200 % zoom) and attention filter (full / skim / low-vision) are applied here,
so simulated users *cannot* see what their real counterparts could not.
"""
from __future__ import annotations

import base64
import hashlib
import io
import json
import os
import random
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional
from urllib.parse import urlparse

from playwright.sync_api import Error as PWError
from playwright.sync_api import Page, TimeoutError as PWTimeout, sync_playwright

try:
    from PIL import Image, ImageFilter
except Exception:  # pragma: no cover
    Image = None

_OBSERVE_JS = (Path(__file__).parent / "observe.js").read_text()

PIXEL_UA = (
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Mobile Safari/537.36"
)
DEVICE_PROFILES: dict[str, dict] = {
    "desktop": dict(viewport={"width": 1280, "height": 800}, device_scale_factor=1),
    "mobile": dict(
        viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True, user_agent=PIXEL_UA
    ),
    # 200 % browser zoom on a 1280x800 screen == 640x400 CSS px rendered at 2x.
    "zoom200": dict(viewport={"width": 640, "height": 400}, device_scale_factor=2),
}

IMAGE_EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif")
VIDEO_EXT = (".mp4", ".webm", ".mov", ".m4v")
MAX_FILE_PAGES = 48

CHALLENGE_HOSTS = ("challenges.cloudflare.com", "hcaptcha.com", "recaptcha", "google.com/recaptcha")
AUTH_HOSTS = ("clerk.", "accounts.google.com", "auth0.com", "stripe.com", "challenges.cloudflare.com")

_SECRET_PARAM = re.compile(r"([?&#](?:[\w-]*token|code|key|sig|signature|jwt|x-amz-[\w-]+|session[\w-]*)=)[^&#\s\"']+", re.I)
_JWT = re.compile(r"\beyJ[\w-]{10,}\.[\w-]{10,}\.[\w-]*")


def redact_secrets(text: str) -> str:
    """Blank out tokens, codes and signatures in URLs and logs so run records can be shared."""
    return _JWT.sub("<redacted-jwt>", _SECRET_PARAM.sub(r"\1<redacted>", text or ""))


# ----------------------------------------------------------------- safety
@dataclass
class SafetyPolicy:
    """Guard-rails for running autonomous agents on production websites.

    Hard blocks can never be lifted; soft blocks (any control showing a price) can be lifted by a
    site config's ``allow_click_patterns``, e.g. to spend a new account's free starter credits.
    """

    blocked_click_patterns: list[str] = field(
        default_factory=lambda: [
            r"\bpay\b",
            r"\bpay now\b",
            r"\bbuy( now)?\b",
            r"\bpurchase\b",
            r"\b(place|confirm|complete|submit)\s+(my\s+)?(order|purchase|payment)\b",
            r"\bsubscribe\b",
            r"\bupgrade\b",
            r"\b(add|buy|get|top[- ]?up)\s+(more\s+)?credits?\b",
            r"\badd (a )?(card|payment)",
            r"\bdelete (my )?account\b",
        ]
    )
    soft_blocked_click_patterns: list[str] = field(default_factory=lambda: [r"[$£€]\s?\d"])
    allowed_click_patterns: list[str] = field(default_factory=list)
    blocked_field_patterns: list[str] = field(
        default_factory=lambda: [r"card", r"\bcvc\b", r"\bcvv\b", r"security code", r"\biban\b", r"sort code", r"account number", r"expir"]
    )
    allowed_domains: list[str] = field(default_factory=list)

    def check_click(self, name: str) -> Optional[str]:
        n = (name or "").lower()
        for p in self.blocked_click_patterns:
            if re.search(p, n, re.I):
                return f"blocked by safety policy (would spend money or be irreversible: matches /{p}/)"
        if any(re.search(p, n, re.I) for p in self.allowed_click_patterns):
            return None
        for p in self.soft_blocked_click_patterns:
            if re.search(p, n, re.I):
                return f"blocked by safety policy (this button shows a price: matches /{p}/)"
        return None

    def check_field(self, info: dict) -> Optional[str]:
        hay = " ".join(str(info.get(k, "")) for k in ("name", "placeholder", "type", "autocomplete")).lower()
        if "cc-" in hay:
            return "blocked by safety policy (payment card field)"
        for p in self.blocked_field_patterns:
            if re.search(p, hay, re.I):
                return f"blocked by safety policy (payment/banking field matches /{p}/)"
        return None

    def domain_allowed(self, url: str) -> bool:
        host = urlparse(url).hostname or ""
        if not self.allowed_domains:
            return True
        return any(host == d or host.endswith("." + d) for d in self.allowed_domains) or any(a in host for a in AUTH_HOSTS)


# ------------------------------------------------------------ observation
@dataclass
class Observation:
    url: str
    title: str
    text: str
    elements: dict[int, dict]
    images: list[dict]
    headings: list[str]
    dialogs: list[str]
    a11y: dict
    page_key: str
    lang: str = ""
    viewport: dict = field(default_factory=dict)
    screenshot: Optional[bytes] = None
    events: list[str] = field(default_factory=list)
    frames: list[dict] = field(default_factory=list)
    full_text: str = ""

    def summary(self) -> dict:
        return {
            "url": self.url,
            "title": self.title,
            "page_key": self.page_key,
            "headings": self.headings,
            "dialogs": self.dialogs,
            "n_elements": len(self.elements),
            "events": self.events,
        }


@dataclass
class ActionResult:
    action: dict
    ok: bool
    message: str = ""
    navigated: bool = False
    data: dict = field(default_factory=dict)

    def to_json(self) -> dict:
        return {"action": self.action, "ok": self.ok, "message": self.message, "navigated": self.navigated, **({"data": self.data} if self.data else {})}


def page_key_for(url: str, headings: list[str], dialogs: list[str]) -> str:
    u = urlparse(url)
    path = re.sub(r"/[0-9a-f]{8,}|/\d{3,}", "/:id", u.path or "/")
    frag = u.fragment.split("?")[0]
    head = (headings[0] if headings else "")[:60]
    dlg = (dialogs[0] if dialogs else "")[:40]
    return f"{u.netloc}{path}{'#' + frag if frag else ''} | {head}{' | dialog: ' + dlg if dlg else ''}"


class BrowserEnv:
    def __init__(
        self,
        run_dir: Path,
        device: str = "desktop",
        headless: bool = False,
        executable_path: Optional[str] = "/usr/local/bin/google-chrome",
        storage_state: Optional[Path] = None,
        safety: Optional[SafetyPolicy] = None,
        assets: Optional[dict[str, Path]] = None,
        inbox: Any = None,
        locale: str = "en-GB",
        action_delay: tuple[float, float] = (0.4, 1.0),
        record_video: bool = False,
        auto_captcha: bool = True,
        timezone_id: Optional[str] = None,
    ):
        self.run_dir = Path(run_dir)
        (self.run_dir / "screenshots").mkdir(parents=True, exist_ok=True)
        (self.run_dir / "artifacts").mkdir(parents=True, exist_ok=True)
        self.device = device
        self.headless = headless
        self.executable_path = executable_path if executable_path and Path(executable_path).exists() else None
        self.storage_state = storage_state
        self.safety = safety or SafetyPolicy()
        self.assets = assets or {}
        self.inbox = inbox
        self.locale = locale
        self.action_delay = action_delay
        self.record_video = record_video
        self.auto_captcha = auto_captcha
        self.timezone_id = timezone_id
        self.challenge_log: list[dict] = []
        self._challenge_clicks: dict[str, int] = {}
        self._frame_ids: dict[str, int] = {}
        self._pw = None
        self.browser = None
        self.context = None
        self.page: Optional[Page] = None
        self._events: list[str] = []
        self.http_errors: list[dict] = []
        self.console_errors: list[str] = []
        self.page_loads: list[dict] = []
        self._last_obs: Optional[Observation] = None
        self._capture_count = 0
        self._downloads: list = []
        self._pdf_tabs: list[tuple[Page, Optional[Page]]] = []
        self._new_tabs: list[tuple[Page, Optional[Page]]] = []
        self._files_seen: set[str] = set()
        self._srcs_seen: set[str] = set()
        self.files: list[dict] = []

    # --------------------------------------------------------------- setup
    def start(self) -> None:
        self._pw = sync_playwright().start()
        args = ["--disable-blink-features=AutomationControlled", "--no-first-run", "--no-default-browser-check"]
        launch_env = None
        if self.locale:
            # Set the language on the browser itself, not via CDP locale emulation: emulation does not
            # reach web workers, and a window/worker navigator.language mismatch makes CAPTCHAs
            # (e.g. Cloudflare Turnstile) reject the browser.
            base = self.locale.split("-")[0]
            args += [f"--lang={self.locale}", f"--accept-lang={self.locale},{base}"]
            launch_env = {**os.environ, "LANGUAGE": f"{self.locale.replace('-', '_')}:{base}", "LANG": f"{self.locale.replace('-', '_')}.UTF-8"}
        self.browser = self._pw.chromium.launch(
            headless=self.headless,
            executable_path=self.executable_path,
            args=args,
            ignore_default_args=["--enable-automation"],
            env=launch_env,
        )
        prof = dict(DEVICE_PROFILES[self.device])
        ctx_kw: dict[str, Any] = dict(prof, accept_downloads=True)
        if self.timezone_id:
            ctx_kw["timezone_id"] = self.timezone_id
        if self.storage_state and Path(self.storage_state).exists():
            ctx_kw["storage_state"] = str(self.storage_state)
        if self.record_video:
            ctx_kw["record_video_dir"] = str(self.run_dir / "video")
            ctx_kw["record_video_size"] = prof["viewport"]
        self.context = self.browser.new_context(**ctx_kw)
        self.page = self.context.new_page()
        self._wire(self.page)
        self.context.on("page", self._on_new_page)

    def _wire(self, page: Page) -> None:
        page.on("dialog", self._on_dialog)
        page.on("response", self._on_response)
        page.on("console", lambda m: self.console_errors.append(redact_secrets(m.text)[:300]) if m.type == "error" else None)
        page.on("download", lambda d: self._downloads.append(d))

    def _on_new_page(self, page: Page) -> None:
        # Waiting for the tab to load here would block inside Playwright's event dispatch and let the agent
        # observe a half-loaded tab (e.g. a slow PDF viewer); tabs are classified in _triage_tabs instead.
        self._new_tabs.append((page, self.page))
        self._wire(page)
        self.page = page

    def _triage_tabs(self) -> None:
        while self._new_tabs:
            page, opener = self._new_tabs.pop(0)
            if page.is_closed():
                if self.page is page and opener is not None and not opener.is_closed():
                    self.page = opener
                continue
            deadline = time.time() + 20
            while page.url in ("", "about:blank") and time.time() < deadline:
                page.wait_for_timeout(250)
            try:
                page.wait_for_load_state("domcontentloaded", timeout=max(1000, int((deadline - time.time()) * 1000)))
            except PWError:
                pass
            if self._is_pdf(page):
                self._pdf_tabs.append((page, opener))
            else:
                self._events.append(f"A new browser tab opened ({page.url}); you are now looking at it.")

    @staticmethod
    def _is_pdf(page: Page) -> bool:
        try:
            return urlparse(page.url).path.lower().endswith(".pdf") or page.evaluate("document.contentType") == "application/pdf"
        except PWError:
            return False

    def _on_dialog(self, dialog) -> None:
        self._events.append(f'A browser pop-up ({dialog.type}) said: "{dialog.message[:300]}" (it was accepted)')
        try:
            dialog.accept()
        except PWError:
            pass

    def _on_response(self, resp) -> None:
        try:
            if resp.status >= 400 and resp.request.resource_type in ("document", "xhr", "fetch"):
                self.http_errors.append({"url": redact_secrets(resp.url)[:200], "status": resp.status, "t": time.time()})
        except PWError:
            pass

    def close(self) -> None:
        for fn in (lambda: self.context and self.context.close(), lambda: self.browser and self.browser.close(), lambda: self._pw and self._pw.stop()):
            try:
                fn()
            except Exception:
                pass

    def save_storage_state(self, path: Path) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.context.storage_state(path=str(path))

    # ------------------------------------------------------------ helpers
    def goto(self, url: str) -> ActionResult:
        t0 = time.time()
        try:
            self.page.goto(url, wait_until="domcontentloaded", timeout=45000)
        except PWTimeout:
            return ActionResult({"type": "goto", "url": url}, False, "page took too long to load")
        self._settle()
        self.page_loads.append({"url": redact_secrets(self.page.url), "seconds": round(time.time() - t0, 2)})
        return ActionResult({"type": "goto", "url": url}, True, f"opened {self.page.url}", navigated=True)

    def _settle(self, quiet_ms: int = 500, max_ms: int = 6000) -> None:
        try:
            self.page.wait_for_load_state("domcontentloaded", timeout=15000)
        except PWError:
            pass
        try:
            self.page.wait_for_load_state("networkidle", timeout=3500)
        except PWError:
            pass
        try:
            self.page.evaluate(
                """([quiet, max]) => new Promise(res => {
                    let t = setTimeout(done, quiet); const start = Date.now();
                    const mo = new MutationObserver(() => { clearTimeout(t); if (Date.now() - start > max) done(); else t = setTimeout(done, quiet); });
                    function done() { mo.disconnect(); res(true); }
                    mo.observe(document.documentElement, {subtree: true, childList: true, characterData: true, attributes: false});
                })""",
                [quiet_ms, max_ms],
            )
        except PWError:
            pass

    def screenshot(self, full_page: bool = False, blur: float = 0.0, max_width: int = 1280, quality: int = 60) -> bytes:
        raw = self.page.screenshot(type="jpeg", quality=quality, full_page=full_page)
        if Image is None:
            return raw
        img = Image.open(io.BytesIO(raw))
        if img.width > max_width:
            img = img.resize((max_width, int(img.height * max_width / img.width)))
        if blur:
            img = img.filter(ImageFilter.GaussianBlur(radius=blur))
        buf = io.BytesIO()
        img.convert("RGB").save(buf, "JPEG", quality=quality)
        return buf.getvalue()

    def _frames_info(self) -> list[dict]:
        out = []
        for f in self.page.frames[1:]:
            host = urlparse(f.url).hostname or ""
            if not host:
                continue
            challenge = any(h in f.url for h in CHALLENGE_HOSTS)
            try:
                el = f.frame_element()
                box = el.bounding_box()
                uqa = None if challenge else el.get_attribute("data-uqa-id")
            except PWError:
                box, uqa = None, None
            if not box or box["width"] < 20:
                continue
            txt = ""
            if not challenge:  # never run script inside CAPTCHA frames: challenge scripts detect it and fail
                try:
                    txt = f.evaluate("document.body ? document.body.innerText.slice(0, 200) : ''")
                except PWError:
                    pass
            fid = self._frame_ids.get(f.url) if challenge else (int(uqa) if uqa else None)
            out.append({"host": host, "url": f.url, "box": box, "id": fid, "text": re.sub(r"\s+", " ", txt).strip(),
                        "challenge": challenge, "handle": el})
        return out

    def _main_signature(self) -> str:
        try:
            t = self.page.evaluate("document.body ? document.body.innerText : ''")
        except PWError:
            t = ""
        return hashlib.md5((self.page.url + t).encode()).hexdigest()

    def _challenge_token(self) -> bool:
        try:
            return bool(self.page.evaluate("() => { const i = document.querySelector('[name=cf-turnstile-response],[name=g-recaptcha-response],[name=h-captcha-response]'); return !!(i && i.value); }"))
        except PWError:
            return False

    def _handle_challenges(self, max_clicks: int = 3, resolve_s: float = 12.0) -> None:
        """Tick 'verify you are human' widgets straight away, as a person would.

        The widget can expire while the model is thinking, so ticking it is treated as a reflex of the
        environment rather than a decision of the agent; every click and its outcome are logged. The
        widget's own content is unreadable (closed shadow DOM), so success is judged from the host page:
        the frame goes away, the page moves on, or a challenge token appears.
        """
        frames = [f for f in self._frames_info() if f["challenge"]]
        if not frames or self._challenge_token():
            return
        fr = frames[0]
        n = self._challenge_clicks.get(fr["url"], 0)
        if n >= max_clicks:
            return
        before = self._main_signature()
        time.sleep(random.uniform(0.8, 1.6) if n == 0 else 0.3)
        b = fr["box"]
        self._human_move_click(b["x"] + 30, b["y"] + b["height"] / 2)
        self._challenge_clicks[fr["url"]] = n + 1
        self._events.append('A "Verify you are human" security check appeared and you ticked its box.')
        t0 = time.time()
        while time.time() - t0 < resolve_s:
            time.sleep(1.0)
            try:
                body = self.page.evaluate("document.body ? document.body.innerText : ''").lower()
            except PWError:
                body = ""
            failed = re.search(r"captcha (failed|error)|verification failed|security check failed|unsupported browser", body)
            if failed:
                self.challenge_log.append({"t": round(t0, 1), "result": "failed", "click": n + 1, "message": failed.group(0)})
                return
            gone = not any(f["challenge"] for f in self._frames_info())
            if self._challenge_token() or (gone and self._main_signature() != before):
                self.challenge_log.append({"t": round(t0, 1), "result": "passed", "click": n + 1, "seconds": round(time.time() - t0, 1)})
                self._events.append("The security check accepted you.")
                self._settle()
                return
        self.challenge_log.append({"t": round(t0, 1), "result": "unresolved", "click": n + 1, "seconds": resolve_s})

    # ---------------------------------------------------------- observing
    def observe(self, attention: str = "full", max_text: int = 9000, with_screenshot: bool = True, include_full_text: bool = True) -> Observation:
        self._settle(quiet_ms=300, max_ms=3000)
        if self.auto_captcha:
            try:
                self._handle_challenges()
            except PWError:
                pass
        raw = None
        for _ in range(3):
            try:
                raw = self.page.evaluate(_OBSERVE_JS, {"maxText": max_text, "attention": attention, "includeFullText": include_full_text})
                break
            except PWError:
                time.sleep(1.0)
                self._settle()
        if raw is None:
            raw = {"url": self.page.url, "title": "", "text": "(the page could not be read)", "elements": [], "images": [],
                   "headings": [], "dialogs": [], "a11y": {}, "viewport": {}}
        frames = self._frames_info()
        known = {e["id"] for e in raw.get("elements", [])}
        for fr in frames:
            if fr["id"] is None or (fr["challenge"] and fr["id"] not in known):
                # Frames inside closed shadow roots (e.g. CAPTCHA widgets) are invisible to observe.js.
                # CAPTCHA frames are never tagged in the DOM; their ids live only on this side.
                try:
                    if fr["id"] is None:
                        fr["id"] = int(self.page.evaluate("() => window.__uqaNext++"))
                        if fr["challenge"]:
                            self._frame_ids[fr["url"]] = fr["id"]
                        elif fr.get("handle") is not None:
                            fr["handle"].evaluate("(e, id) => e.setAttribute('data-uqa-id', String(id))", fr["id"])
                    raw.setdefault("elements", []).append(
                        {"id": fr["id"], "role": "iframe", "tag": "iframe", "name": "security check" if fr["challenge"] else "embedded frame",
                         "src": fr["host"], "frame_url": fr["url"],
                         "bbox": [round(fr["box"]["x"]), round(fr["box"]["y"]), round(fr["box"]["width"]), round(fr["box"]["height"])]}
                    )
                except PWError:
                    pass
        text = raw["text"]
        for fr in frames:
            label = "security check (CAPTCHA) widget" if fr["challenge"] else "embedded frame"
            if fr["challenge"] and self._challenge_clicks.get(fr["url"]):
                label += " (you have already ticked it)"
            ref = f"[{fr['id']}]" if fr["id"] else "(no id)"
            text += f"\n{ref} iframe {label} from {fr['host']}" + (f': "{fr["text"][:120]}"' if fr["text"] else "")
        shot = None
        if with_screenshot:
            try:
                shot = self.screenshot(blur=1.6 if attention == "low_vision" else 0.0, max_width=1280 if self.device != "mobile" else 780)
            except PWError:
                shot = None
        obs = Observation(
            url=raw["url"],
            title=raw.get("title", ""),
            text=text,
            elements={e["id"]: e for e in raw.get("elements", [])},
            images=raw.get("images", []),
            headings=raw.get("headings", []),
            dialogs=raw.get("dialogs", []),
            a11y=raw.get("a11y", {}),
            page_key=page_key_for(raw["url"], raw.get("headings", []), raw.get("dialogs", [])),
            lang=raw.get("lang", ""),
            viewport=raw.get("viewport", {}),
            screenshot=shot,
            events=self._events[:],
            frames=frames,
            full_text=raw.get("fullText") or "",
        )
        self._events.clear()
        self._last_obs = obs
        return obs

    def save_screenshot(self, data: bytes, name: str) -> str:
        p = self.run_dir / "screenshots" / name
        p.write_bytes(data)
        return str(p.relative_to(self.run_dir))

    # ------------------------------------------------------------ actions
    def _loc(self, el_id: int):
        return self.page.locator(f'[data-uqa-id="{el_id}"]').first

    @staticmethod
    def _label(info: dict, n: int = 60) -> str:
        return (info.get("name") or info.get("placeholder") or "")[:n]

    def _info(self, el_id: Any) -> Optional[dict]:
        if self._last_obs is None:
            return None
        try:
            return self._last_obs.elements.get(int(el_id))
        except (TypeError, ValueError):
            return None

    def execute(self, action: dict) -> ActionResult:
        kind = (action.get("type") or "").lower()
        handler: Optional[Callable[[dict], ActionResult]] = getattr(self, f"_act_{kind}", None)
        if handler is None:
            return ActionResult(action, False, f"unknown action type {kind!r}")
        url_before = self.page.url
        try:
            res = handler(action)
        except PWTimeout as e:
            res = ActionResult(action, False, f"timed out: {str(e).splitlines()[0][:160]}")
        except PWError as e:
            res = ActionResult(action, False, f"browser error: {str(e).splitlines()[0][:160]}")
        if kind not in ("wait", "wait_for_change", "read_inbox", "done", "give_up", "read_page", "capture_output", "flip_through"):
            self._settle()
            time.sleep(random.uniform(*self.action_delay))
        if self.page.url != url_before:
            res.navigated = True
            if not self.safety.domain_allowed(self.page.url):
                res.message += f" | NOTE: you are now on a different website ({urlparse(self.page.url).hostname})."
        return res

    def _click_iframe(self, info: dict) -> ActionResult:
        fr = next((f for f in self._frames_info() if f["id"] == info["id"]), None)
        box = fr["box"] if fr else self._loc(info["id"]).bounding_box()
        if not box:
            return ActionResult({"type": "click", "id": info["id"]}, False, "frame not found")
        challenge = bool(fr and fr["challenge"])
        x = box["x"] + (30 if challenge else box["width"] / 2)
        y = box["y"] + box["height"] / 2
        self._human_move_click(x, y)
        time.sleep(4 if challenge else 1)
        return ActionResult({"type": "click", "id": info["id"]}, True, "clicked the " + ("security check box" if challenge else "embedded frame"))

    def _human_move_click(self, x: float, y: float) -> None:
        self.page.mouse.move(x - random.uniform(60, 160), y - random.uniform(20, 70), steps=random.randint(8, 14))
        time.sleep(random.uniform(0.15, 0.35))
        self.page.mouse.move(x, y, steps=random.randint(12, 22))
        time.sleep(random.uniform(0.1, 0.3))
        self.page.mouse.click(x, y)

    def _act_click(self, a: dict) -> ActionResult:
        if "x" in a and "y" in a and "id" not in a:
            self._human_move_click(float(a["x"]), float(a["y"]))
            return ActionResult(a, True, f"clicked at ({a['x']}, {a['y']})")
        info = self._info(a.get("id"))
        if not info:
            return ActionResult(a, False, f"there is no element [{a.get('id')}] on the current page")
        reason = self.safety.check_click(info.get("name", ""))
        if reason:
            return ActionResult(a, False, reason)
        if info["role"] == "iframe":
            return self._click_iframe(info)
        loc = self._loc(info["id"])
        try:
            loc.scroll_into_view_if_needed(timeout=3000)
        except PWError:
            pass
        try:
            loc.click(timeout=5000)
            return ActionResult(a, True, f'clicked {info["role"]} "{self._label(info)}"')
        except PWError as e:
            err = str(e).splitlines()[0][:120]
        # Fallbacks: label of a hidden input, then a DOM click.
        try:
            ok = loc.evaluate(
                "el => { if (el.labels && el.labels.length) { el.labels[0].click(); return 'label'; } el.click(); return 'dom'; }"
            )
            return ActionResult(a, True, f'clicked {info["role"]} "{self._label(info)}" (via {ok})')
        except PWError:
            return ActionResult(a, False, f"could not click: {err}")

    def _act_type(self, a: dict) -> ActionResult:
        info = self._info(a.get("id"))
        if not info:
            return ActionResult(a, False, f"there is no element [{a.get('id')}] on the current page")
        reason = self.safety.check_field(info)
        if reason:
            return ActionResult(a, False, reason)
        text = str(a.get("text", ""))
        loc = self._loc(info["id"])
        loc.scroll_into_view_if_needed(timeout=3000)
        if a.get("clear", True):
            try:
                loc.fill("", timeout=4000)
            except PWError:
                loc.click(timeout=4000)
                self.page.keyboard.press("Control+A")
                self.page.keyboard.press("Delete")
        if len(text) <= 140:
            loc.click(timeout=4000)
            self.page.keyboard.type(text, delay=random.randint(18, 45))
        else:
            loc.fill(text, timeout=8000)
        if a.get("enter"):
            self.page.keyboard.press("Enter")
        msg = f'typed {len(text)} characters into {info["role"]} "{self._label(info, 50)}"'
        data = {}
        try:
            val = loc.input_value(timeout=2000)
            if info.get("type") != "password" and len(val) < len(text):
                msg += f" -- but the box now only shows {len(val)} characters; the end of what you typed was cut off: ...{val[-60:]!r}"
                data["truncated_to"] = len(val)
        except PWError:
            pass
        return ActionResult(a, True, msg, data=data)

    def _act_select(self, a: dict) -> ActionResult:
        info = self._info(a.get("id"))
        if not info:
            return ActionResult(a, False, f"there is no element [{a.get('id')}] on the current page")
        option = str(a.get("option", a.get("value", "")))
        loc = self._loc(info["id"])
        try:
            loc.select_option(label=option, timeout=4000)
        except PWError:
            opts = loc.evaluate("el => Array.from(el.options).map(o => [o.value, o.text.trim()])")
            match = next((v for v, t in opts if option.lower() in t.lower() or option.lower() == v.lower()), None)
            if match is None:
                return ActionResult(a, False, f"no option like {option!r}; options are {[t for _, t in opts][:15]}")
            loc.select_option(value=match, timeout=4000)
        return ActionResult(a, True, f'selected "{option}"')

    def _act_set_range(self, a: dict) -> ActionResult:
        info = self._info(a.get("id"))
        if not info:
            return ActionResult(a, False, f"there is no element [{a.get('id')}] on the current page")
        val = str(a.get("value"))
        self._loc(info["id"]).evaluate(
            """(el, v) => { const s = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
                s.call(el, v); el.dispatchEvent(new Event('input', {bubbles: true})); el.dispatchEvent(new Event('change', {bubbles: true})); }""",
            val,
        )
        return ActionResult(a, True, f"moved the slider to {val}")

    def _act_upload(self, a: dict) -> ActionResult:
        info = self._info(a.get("id"))
        name = str(a.get("file", ""))
        path = self.assets.get(name) or next((p for k, p in self.assets.items() if name.lower() in k.lower()), None)
        if not path:
            return ActionResult(a, False, f"you have no file called {name!r}; your files: {list(self.assets)}")
        if not info:
            return ActionResult(a, False, f"there is no element [{a.get('id')}] on the current page")
        loc = self._loc(info["id"])
        if info.get("type") == "file" or info["role"] == "file-upload":
            loc.set_input_files(str(path), timeout=5000)
        else:
            with self.page.expect_file_chooser(timeout=6000) as fc:
                loc.click(timeout=4000)
            fc.value.set_files(str(path))
        return ActionResult(a, True, f"chose the file {name}")

    def _act_scroll(self, a: dict) -> ActionResult:
        if a.get("id") is not None and self._info(a.get("id")):
            self._loc(int(a["id"])).scroll_into_view_if_needed(timeout=3000)
            return ActionResult(a, True, f"scrolled to [{a['id']}]")
        direction = -1 if str(a.get("direction", "down")).lower() == "up" else 1
        amount = 0.85 if a.get("amount", "page") == "page" else 0.45
        self.page.evaluate("([d, f]) => window.scrollBy({top: d * window.innerHeight * f, behavior: 'instant'})", [direction, amount])
        time.sleep(0.4)
        return ActionResult(a, True, f"scrolled {'up' if direction < 0 else 'down'}")

    def _act_press(self, a: dict) -> ActionResult:
        key = str(a.get("key", "Enter"))
        self.page.keyboard.press(key)
        return ActionResult(a, True, f"pressed {key}")

    def _act_go_back(self, a: dict) -> ActionResult:
        self.page.go_back(wait_until="domcontentloaded", timeout=20000)
        return ActionResult(a, True, "went back")

    def _act_goto(self, a: dict) -> ActionResult:
        url = str(a.get("url", ""))
        if self._last_obs and not urlparse(url).scheme:
            url = urlparse(self._last_obs.url)._replace(path=url, query="", fragment="").geturl()
        if not self.safety.domain_allowed(url):
            return ActionResult(a, False, f"navigation outside the site under test is not allowed ({url})")
        return self.goto(url)

    def _act_wait(self, a: dict) -> ActionResult:
        s = max(1.0, min(float(a.get("seconds", 5)), 90.0))
        time.sleep(s)
        return ActionResult(a, True, f"waited {s:.0f} seconds")

    def _act_wait_for_change(self, a: dict) -> ActionResult:
        """Wait (without spending LLM calls) until the page content changes, e.g. an AI generation finishing."""
        max_s = max(5.0, min(float(a.get("max_seconds", 120)), 600.0))
        until = str(a.get("until_text", "") or "").lower()
        t0 = time.time()

        def sig() -> str:
            try:
                t = self.page.evaluate("document.body ? document.body.innerText : ''")
            except PWError:
                t = ""
            t = re.sub(r"\d+\s*%|\d+:\d\d|\d+ ?s(ec)?\b", "", t)  # ignore ticking progress counters
            return hashlib.md5((self.page.url + t).encode()).hexdigest(), t.lower()

        start_sig, _ = sig()
        last = start_sig
        stable_since = None
        while time.time() - t0 < max_s:
            time.sleep(3)
            s, txt = sig()
            if until and until in txt:
                return ActionResult(a, True, f'"{until}" appeared after {time.time() - t0:.0f} s', data={"waited_s": round(time.time() - t0, 1)})
            if s != start_sig and not until:
                if s == last:
                    stable_since = stable_since or time.time()
                    if time.time() - stable_since >= 3:
                        return ActionResult(a, True, f"the page changed after {time.time() - t0:.0f} s", data={"waited_s": round(time.time() - t0, 1)})
                else:
                    stable_since = None
            last = s
        return ActionResult(a, True, f"nothing changed after waiting {max_s:.0f} s", data={"waited_s": max_s, "timeout": True})

    def _act_read_inbox(self, a: dict) -> ActionResult:
        if self.inbox is None:
            return ActionResult(a, False, "you don't have access to an e-mail inbox in this session")
        msg = self.inbox.wait_for_message(timeout=float(a.get("max_seconds", 90)))
        if not msg:
            return ActionResult(a, True, "your inbox has no new e-mail yet")
        body = msg["text"][:600]
        return ActionResult(
            a, True, f'New e-mail from {msg["from"]}: subject "{msg["subject"]}". It says: "{body}"', data={"code": msg.get("code")}
        )

    def _act_read_page(self, a: dict) -> ActionResult:
        return ActionResult(a, True, "you read the whole page carefully (full text will be shown)")

    def _act_done(self, a: dict) -> ActionResult:
        return ActionResult(a, True, "finished")

    def _act_give_up(self, a: dict) -> ActionResult:
        return ActionResult(a, True, "gave up")

    # ------------------------------------------------------ output capture
    def capture_output(self, label: str = "", max_views: int = 6) -> dict:
        """Capture the generated content currently shown (text + large images + viewport shots)."""
        self._capture_count += 1
        cdir = self.run_dir / "artifacts" / f"capture_{self._capture_count:02d}"
        cdir.mkdir(parents=True, exist_ok=True)
        self._settle()
        text = self.page.evaluate("document.body.innerText")
        (cdir / "text.txt").write_text(text)
        shots = []
        vp = self.page.viewport_size or {"height": 800}
        total = self.page.evaluate("document.documentElement.scrollHeight")
        y0 = self.page.evaluate("window.scrollY")
        n = min(max_views, max(1, int(total / vp["height"]) + 1))
        for i in range(n):
            self.page.evaluate("y => window.scrollTo(0, y)", y0 + i * vp["height"] if max_views == 1 else i * vp["height"])
            time.sleep(0.5)
            data = self.screenshot(max_width=1100, quality=65)
            p = cdir / f"view_{i:02d}.jpg"
            p.write_bytes(data)
            shots.append(str(p.relative_to(self.run_dir)))
        self.page.evaluate("y => window.scrollTo(0, y)", y0)
        imgs = []
        handles = self.page.query_selector_all("img, canvas, svg")
        self._toggle_overlays(hide=True)
        try:
            for h in handles:
                if len(imgs) >= 16:
                    break
                try:
                    box = h.bounding_box()
                    if not box or box["width"] < 180 or box["height"] < 140:
                        continue
                    h.scroll_into_view_if_needed(timeout=2000)
                    time.sleep(0.2)
                    p = cdir / f"img_{len(imgs):02d}.jpg"
                    h.screenshot(path=str(p), type="jpeg", quality=70, timeout=5000)
                    alt = h.get_attribute("alt") or h.get_attribute("aria-label") or ""
                    imgs.append({"path": str(p.relative_to(self.run_dir)), "alt": alt, "w": round(box["width"]), "h": round(box["height"])})
                except PWError:
                    continue
        finally:
            self._toggle_overlays(hide=False)
        self.page.evaluate("y => window.scrollTo(0, y)", y0)
        cap = {"label": label, "url": self.page.url, "text": text[:30000], "views": shots, "images": imgs, "dir": str(cdir.relative_to(self.run_dir))}
        (cdir / "capture.json").write_text(json.dumps({k: v for k, v in cap.items() if k != "text"}, indent=2))
        return cap

    # --------------------------------------------------------- file outputs
    def collect_file_outputs(self) -> list[dict]:
        """Turn files the site produced (downloads, PDFs opened in a tab or embedded in the page) into captures.

        A person would open such a file and look through it, so each page / frame becomes a capture that
        the output assessment reviews like any on-page output.
        """
        caps: list[dict] = []
        try:
            self.page.wait_for_timeout(100)  # the sync API only delivers queued events (new tabs, downloads) inside a call
        except PWError:
            pass
        self._triage_tabs()
        while self._downloads:
            d = self._downloads.pop(0)
            name = re.sub(r"[^\w.\-]+", "_", d.suggested_filename or "download")
            path = self._file_path(name)
            try:
                d.save_as(str(path))
            except PWError as e:
                self._events.append(f'The download "{name}" failed ({str(e).splitlines()[0][:80]}).')
                continue
            caps += self._file_captures(path, origin=d.url, how="downloaded")
        while self._pdf_tabs:
            tab, opener = self._pdf_tabs.pop(0)
            data = self._fetch_bytes(tab.url, [opener, tab])
            if data and data[:4] == b"%PDF":
                path = self._file_path("document.pdf" if tab.url.startswith("blob:") else (Path(urlparse(tab.url).path).name or "document.pdf"), ".pdf")
                path.write_bytes(data)
                caps += self._file_captures(path, origin=tab.url, how="opened in a new tab")
            if opener is not None and not opener.is_closed():
                try:
                    tab.close()
                except PWError:
                    pass
                self.page = opener
                self._events.append("You finished reading the PDF and went back to the website's tab.")
        if self._is_pdf(self.page):
            url = self.page.url
            data = self._fetch_bytes(url, [self.page])
            if data and data[:4] == b"%PDF":
                path = self._file_path(Path(urlparse(url).path).name or "document.pdf", ".pdf")
                path.write_bytes(data)
                caps += self._file_captures(path, origin=url, how="opened in this tab")
            try:
                if self.page.go_back(wait_until="domcontentloaded", timeout=15000) is not None:
                    self._events.append("You finished reading the PDF and went back to the previous page.")
            except PWError:
                pass
        try:
            srcs = self.page.evaluate(
                "Array.from(document.querySelectorAll('embed,object,iframe')).map(e => e.src || e.data || '')"
                ".filter(u => /\\.pdf($|[?#])/i.test(u) || /^blob:/.test(u))"
            )
        except PWError:
            srcs = []
        for src in srcs:
            if src in self._srcs_seen:
                continue
            self._srcs_seen.add(src)
            data = self._fetch_bytes(src, [self.page])
            if data and data[:4] == b"%PDF":
                path = self._file_path(Path(urlparse(src).path).name or "embedded.pdf", ".pdf")
                path.write_bytes(data)
                caps += self._file_captures(path, origin=src, how="shown inside the page")
        return caps

    def _file_path(self, name: str, ext: str = "") -> Path:
        d = self.run_dir / "artifacts" / "files"
        d.mkdir(parents=True, exist_ok=True)
        name = name if not ext or name.lower().endswith(ext) else name + ext
        n = 1 + sum(1 for _ in d.iterdir())
        return d / f"{n:02d}_{name}"

    def _fetch_bytes(self, url: str, pages: list) -> Optional[bytes]:
        if not url.startswith(("blob:", "data:")):
            try:
                r = self.context.request.get(url, timeout=60000)
                if r.ok:
                    return r.body()
            except PWError:
                pass
        for pg in pages:  # blob URLs only resolve inside the page that created them
            if pg is None or pg.is_closed():
                continue
            try:
                b64 = pg.evaluate(
                    """async u => { const b = await (await fetch(u)).blob();
                        return await new Promise(res => { const r = new FileReader(); r.onload = () => res(String(r.result).split(',')[1]); r.readAsDataURL(b); }); }""",
                    url,
                )
                return base64.b64decode(b64)
            except PWError:
                continue
        return None

    def _file_captures(self, path: Path, origin: str = "", how: str = "downloaded") -> list[dict]:
        data = path.read_bytes()
        digest = hashlib.sha1(data).hexdigest()
        if digest in self._files_seen:
            return []
        self._files_seen.add(digest)
        suffix = path.suffix.lower()
        pages: list[tuple[str, bytes]] = []  # (text, jpeg)
        kind = "file"
        try:
            if data[:4] == b"%PDF":
                kind = "PDF"
                import pymupdf

                with pymupdf.open(path) as doc:
                    total = doc.page_count
                    for pg in list(doc)[:MAX_FILE_PAGES]:
                        pix = pg.get_pixmap(matrix=pymupdf.Matrix(1100 / max(pg.rect.width, 1), 1100 / max(pg.rect.width, 1)))
                        buf = io.BytesIO()
                        Image.frombytes("RGB", (pix.width, pix.height), pix.samples).save(buf, "JPEG", quality=70)
                        pages.append((pg.get_text(), buf.getvalue()))
            elif suffix in IMAGE_EXT:
                kind, total = "image", 1
                buf = io.BytesIO()
                im = Image.open(path).convert("RGB")
                im.thumbnail((1400, 1400))
                im.save(buf, "JPEG", quality=75)
                pages.append(("", buf.getvalue()))
            elif suffix in VIDEO_EXT:
                kind = "video"
                pages = self._video_frames(path)
                total = len(pages)
        except Exception as e:  # a broken file is itself a finding, but must not end the session
            self._events.append(f'You tried to open "{path.name[3:]}" but it would not open ({type(e).__name__}).')
            return []
        rec = {"file": str(path.relative_to(self.run_dir)), "kind": kind, "origin": origin[:200], "how": how, "pages": len(pages), "bytes": len(data)}
        self.files.append(rec)
        if not pages:
            self._events.append(f'The site gave you a file "{path.name[3:]}" ({kind}, {len(data) // 1024} KB) that you cannot open here.')
            return []
        caps = []
        for i, (text, jpg) in enumerate(pages):
            self._capture_count += 1
            cdir = self.run_dir / "artifacts" / f"capture_{self._capture_count:02d}"
            cdir.mkdir(parents=True, exist_ok=True)
            (cdir / "text.txt").write_text(text)
            (cdir / "view_00.jpg").write_bytes(jpg)
            w, h = Image.open(io.BytesIO(jpg)).size
            rel = str((cdir / "view_00.jpg").relative_to(self.run_dir))
            unit = "frame" if kind == "video" else "page"
            cap = {"label": f"{path.name[3:]} {unit} {i + 1} of {total}", "url": f"file://{path.name}/{unit}-{i + 1}", "text": text,
                   "views": [rel], "images": [{"path": rel, "alt": f"{kind} {unit} {i + 1}", "w": w, "h": h}],
                   "dir": str(cdir.relative_to(self.run_dir)), "source": "file", "dedupe_key": f"{digest}:{i}"}
            (cdir / "capture.json").write_text(json.dumps({k: v for k, v in cap.items() if k != "text"}, indent=2))
            caps.append(cap)
        first = re.sub(r"\s+", " ", pages[0][0]).strip()[:160]
        self._events.append(
            f'The site gave you a {kind} "{path.name[3:]}" ({how}); you opened it and looked through all {len(pages)} '
            f"{'frames' if kind == 'video' else 'pages'}" + (f'. It begins: "{first}"' if first else ".")
        )
        return caps

    def _video_frames(self, path: Path, n: int = 8) -> list[tuple[str, bytes]]:
        import subprocess

        try:
            dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                                       capture_output=True, text=True, timeout=30).stdout.strip() or 0)
        except (OSError, ValueError, subprocess.SubprocessError):
            dur = 0.0
        frames = []
        for i in range(n if dur > 0 else 1):
            t = dur * (i + 0.5) / n if dur > 0 else 0
            out = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(path), "-frames:v", "1", "-vf", "scale=1000:-2",
                                  "-f", "image2", "-c:v", "mjpeg", "pipe:1"], capture_output=True, timeout=60)
            if out.stdout:
                frames.append((f"(video frame at {t:.0f} s of {dur:.0f} s; the soundtrack/narration is not assessed)", out.stdout))
        return frames

    def _toggle_overlays(self, hide: bool) -> None:
        """Hide fixed/sticky bars so element screenshots of generated images are not occluded."""
        try:
            self.page.evaluate(
                """hide => {
                    if (hide) {
                        for (const el of document.querySelectorAll('body *')) {
                            const p = getComputedStyle(el).position;
                            if (p === 'fixed' || p === 'sticky') { el.dataset.uqaVis = el.style.visibility || '-'; el.style.visibility = 'hidden'; }
                        }
                    } else {
                        for (const el of document.querySelectorAll('[data-uqa-vis]')) {
                            el.style.visibility = el.dataset.uqaVis === '-' ? '' : el.dataset.uqaVis; delete el.dataset.uqaVis;
                        }
                    }
                }""",
                hide,
            )
        except PWError:
            pass

    def flip_through(self, next_id: int, max_pages: int = 40, label: str = "") -> list[dict]:
        """Macro action: repeatedly capture and press a 'next page' control until content stops changing."""
        caps = []
        info = self._info(next_id)
        if not info:
            return caps
        name = info.get("name", "")
        seen = set()
        for i in range(max_pages):
            cur = self.page.evaluate("document.body.innerText")
            h = hashlib.md5(cur.encode()).hexdigest()
            if h in seen:
                break
            seen.add(h)
            caps.append(self.capture_output(label=f"{label} page {i + 1}".strip(), max_views=1))
            loc = self._loc(next_id)
            try:
                if loc.count() == 0 or not loc.is_visible() or loc.is_disabled():
                    alt = self.page.get_by_role("button", name=name).first if name else None
                    if not alt or alt.count() == 0 or alt.is_disabled():
                        break
                    loc = alt
                loc.click(timeout=4000)
            except PWError:
                break
            self._settle(quiet_ms=400, max_ms=4000)
        return caps
