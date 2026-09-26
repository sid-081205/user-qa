"""OpenRouter chat-completions client tuned for agent loops on free models.

Design constraints (see paper, Sec. 4.7):
* Free OpenRouter keys are limited (e.g. 50 ``:free`` requests/day), so every call
  is budgeted, logged and attributable to a purpose (step, output assessment...).
* Free endpoints are flaky (429/5xx, empty completions), so the client retries
  with exponential back-off and falls back through a list of models.
* Agents need structured output, so the client requests JSON mode where the model
  supports it and repairs/extracts JSON leniently otherwise.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Optional

import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = "stealth/space-bunny-alpha"
DEFAULT_FALLBACKS = ["google/gemma-4-31b-it:free", "qwen/qwen3.8-27b:free", "openrouter/free"]


class BudgetExceeded(RuntimeError):
    pass


class LLMError(RuntimeError):
    pass


@dataclass
class LLMUsage:
    calls: int = 0
    failed_calls: int = 0
    prompt_tokens: int = 0
    completion_tokens: int = 0
    seconds: float = 0.0
    by_purpose: dict = field(default_factory=dict)
    by_model: dict = field(default_factory=dict)

    def to_json(self) -> dict:
        return {
            "calls": self.calls,
            "failed_calls": self.failed_calls,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "seconds": round(self.seconds, 1),
            "by_purpose": self.by_purpose,
            "by_model": self.by_model,
        }


def image_part(jpeg_bytes: bytes, mime: str = "image/jpeg", detail: str = "auto") -> dict:
    b64 = base64.b64encode(jpeg_bytes).decode()
    return {"type": "image_url", "image_url": {"url": f"data:{mime};base64,{b64}", "detail": detail}}


def _redact_images(messages: list[dict]) -> list[dict]:
    """Copy of messages with base64 payloads replaced by a short digest (for logs)."""
    out = []
    for m in messages:
        content = m.get("content")
        if isinstance(content, list):
            parts = []
            for p in content:
                if p.get("type") == "image_url":
                    url = p["image_url"]["url"]
                    digest = hashlib.sha1(url.encode()).hexdigest()[:10]
                    parts.append({"type": "image_url", "image_url": f"<image sha1={digest} chars={len(url)}>"})
                else:
                    parts.append(p)
            out.append({**m, "content": parts})
        else:
            out.append(m)
    return out


_FENCE_RE = re.compile(r"```(?:json)?\s*(.*?)```", re.S)


def parse_json_lenient(text: str) -> Any:
    """Extract the first JSON object/array from ``text`` tolerating common LLM quirks."""
    if text is None:
        raise ValueError("empty completion")
    candidates = []
    t = text.strip()
    candidates.append(t)
    for m in _FENCE_RE.finditer(t):
        candidates.append(m.group(1).strip())
    start = min([i for i in (t.find("{"), t.find("[")) if i >= 0], default=-1)
    if start >= 0:
        candidates.append(_balanced_slice(t, start))
    for c in candidates:
        if not c:
            continue
        for variant in (c, _repair(c)):
            try:
                return json.loads(variant)
            except Exception:
                continue
    raise ValueError(f"could not parse JSON from completion: {t[:300]!r}")


def _balanced_slice(t: str, start: int) -> str:
    closers: list[str] = []
    in_str, esc = False, False
    for i in range(start, len(t)):
        ch = t[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in "{[":
            closers.append("}" if ch == "{" else "]")
        elif ch in "}]":
            if closers:
                closers.pop()
            if not closers:
                return t[start : i + 1]
    # A completion cut off by the token limit: close the open string and brackets innermost first.
    return t[start:] + ('"' if in_str else "") + "".join(reversed(closers))


def _repair(s: str) -> str:
    s = re.sub(r",\s*([}\]])", r"\1", s)  # trailing commas
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"(?<!\\)\n", " ", s)  # raw newlines inside strings
    return s


class LLMClient:
    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        fallbacks: Optional[Iterable[str]] = None,
        api_key: Optional[str] = None,
        max_calls: int = 60,
        log_path: Optional[Path] = None,
        temperature: float = 0.7,
        reasoning_effort: Optional[str] = "low",
        timeout: float = 180.0,
        min_interval: float = 0.0,
    ):
        self.model = model
        self.fallbacks = list(fallbacks) if fallbacks is not None else list(DEFAULT_FALLBACKS)
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY", "")
        if not self.api_key:
            raise LLMError("OPENROUTER_API_KEY is not set (put it in .env or the environment)")
        self.max_calls = max_calls
        self.log_path = Path(log_path) if log_path else None
        self.temperature = temperature
        self.reasoning_effort = reasoning_effort
        self.timeout = timeout
        self.min_interval = min_interval
        self.usage = LLMUsage()
        self._last_call = 0.0
        self._model_meta: dict[str, dict] = {}

    # ----------------------------------------------------------------- utils
    @property
    def remaining(self) -> int:
        return self.max_calls - self.usage.calls

    def supports_images(self, model: Optional[str] = None) -> bool:
        meta = self._meta(model or self.model)
        if not meta:
            return True
        return "image" in (meta.get("architecture", {}).get("input_modalities") or [])

    def _meta(self, model: str) -> dict:
        if model in self._model_meta:
            return self._model_meta[model]
        try:
            data = requests.get("https://openrouter.ai/api/v1/models", timeout=30).json()["data"]
            for m in data:
                self._model_meta[m["id"]] = m
        except Exception:
            pass
        return self._model_meta.get(model, {})

    def quota(self) -> dict:
        try:
            r = requests.get(
                "https://openrouter.ai/api/v1/key",
                headers={"Authorization": f"Bearer {self.api_key}"},
                timeout=20,
            )
            return r.json().get("data", {})
        except Exception as e:  # pragma: no cover - network
            return {"error": str(e)}

    def _log(self, record: dict) -> None:
        if not self.log_path:
            return
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        with self.log_path.open("a") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    # ------------------------------------------------------------------ core
    def chat(
        self,
        messages: list[dict],
        *,
        purpose: str = "generic",
        json_mode: bool = True,
        max_tokens: int = 4000,
        temperature: Optional[float] = None,
        reasoning_effort: Optional[str] = "__default__",
        models: Optional[list[str]] = None,
    ) -> tuple[str, dict]:
        """Return ``(content, meta)``. Raises :class:`BudgetExceeded` or :class:`LLMError`."""
        if self.usage.calls >= self.max_calls:
            raise BudgetExceeded(f"LLM call budget of {self.max_calls} exhausted")
        effort = self.reasoning_effort if reasoning_effort == "__default__" else reasoning_effort
        chain = models or [self.model] + [m for m in self.fallbacks if m != self.model]
        errors = []
        for model in chain:
            for attempt in range(3):
                wait = self.min_interval - (time.time() - self._last_call)
                if wait > 0:
                    time.sleep(wait)
                body: dict[str, Any] = {
                    "model": model,
                    "messages": messages,
                    "max_tokens": max_tokens,
                    "temperature": self.temperature if temperature is None else temperature,
                }
                meta = self._meta(model)
                params = set(meta.get("supported_parameters") or [])
                if json_mode and (not params or "response_format" in params):
                    body["response_format"] = {"type": "json_object"}
                if effort and (not params or "reasoning" in params):
                    body["reasoning"] = {"effort": effort}
                t0 = time.time()
                self._last_call = t0
                try:
                    r = requests.post(
                        OPENROUTER_URL,
                        headers={
                            "Authorization": f"Bearer {self.api_key}",
                            "Content-Type": "application/json",
                            "HTTP-Referer": "https://github.com/sid-081205/user-qa",
                            "X-Title": "UserQA persona usability agent",
                        },
                        json=body,
                        timeout=self.timeout,
                    )
                    dt = time.time() - t0
                    data = r.json() if r.content else {}
                except (requests.RequestException, ValueError) as e:
                    dt = time.time() - t0
                    errors.append(f"{model}: {e}")
                    self.usage.failed_calls += 1
                    time.sleep(2 ** attempt * 2)
                    continue
                if r.status_code != 200 or "choices" not in data:
                    err = data.get("error", {}) if isinstance(data, dict) else {}
                    msg = f"{model}: HTTP {r.status_code} {err.get('message', '')[:200]}"
                    errors.append(msg)
                    self.usage.failed_calls += 1
                    self._log({"ts": t0, "purpose": purpose, "model": model, "error": msg, "seconds": round(dt, 2)})
                    if r.status_code in (400, 401, 402, 403, 404):
                        break  # not retryable on this model
                    time.sleep(min(30, 2 ** attempt * 3))
                    continue
                choice = data["choices"][0]
                content = (choice.get("message") or {}).get("content") or ""
                usage = data.get("usage") or {}
                self.usage.calls += 1
                self.usage.prompt_tokens += int(usage.get("prompt_tokens") or 0)
                self.usage.completion_tokens += int(usage.get("completion_tokens") or 0)
                self.usage.seconds += dt
                self.usage.by_purpose[purpose] = self.usage.by_purpose.get(purpose, 0) + 1
                self.usage.by_model[model] = self.usage.by_model.get(model, 0) + 1
                self._log(
                    {
                        "ts": t0,
                        "purpose": purpose,
                        "model": model,
                        "served_model": data.get("model"),
                        "seconds": round(dt, 2),
                        "usage": usage,
                        "finish_reason": choice.get("finish_reason"),
                        "request": _redact_images(messages),
                        "response": content,
                        "reasoning": (choice.get("message") or {}).get("reasoning"),
                    }
                )
                if not content.strip():
                    errors.append(f"{model}: empty completion ({choice.get('finish_reason')})")
                    if self.usage.calls >= self.max_calls:
                        break
                    max_tokens = int(max_tokens * 1.5)
                    continue
                return content, {"model": model, "seconds": dt, "usage": usage}
        raise LLMError("all models failed: " + " | ".join(errors[-6:]))

    def chat_json(self, messages: list[dict], *, purpose: str = "generic", retries: int = 1, **kw) -> tuple[Any, dict]:
        """Chat and parse JSON; on parse failure ask once for a corrected JSON."""
        content, meta = self.chat(messages, purpose=purpose, **kw)
        try:
            return parse_json_lenient(content), meta
        except ValueError as e:
            if retries <= 0 or self.remaining <= 0:
                raise LLMError(str(e)) from e
            fix = messages + [
                {"role": "assistant", "content": content[:6000]},
                {
                    "role": "user",
                    "content": "Your previous reply was not valid JSON. Reply again with ONLY the corrected JSON object, no prose.",
                },
            ]
            return self.chat_json(fix, purpose=purpose + ":repair", retries=retries - 1, **kw)
