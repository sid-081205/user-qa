"""The persona agent: perceive -> think aloud & inspect -> act, with budget-aware batching."""
from __future__ import annotations

import hashlib
import json
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

from ..browser.env import ActionResult, BrowserEnv, Observation
from ..llm import BudgetExceeded, LLMClient, LLMError, image_part
from ..personas.schema import Persona
from . import prompts
from .memory import Memory, StepMemory

INPUT_ACTIONS = {"type", "select", "set_range", "upload"}
TERMINAL = {"done", "give_up"}


@dataclass
class AgentConfig:
    start_url: str
    goal: str
    max_steps: int = 30
    vision: bool = True
    max_actions_per_step: int = 6
    abandon_mode: str = "note"  # "note": record would-abandon and continue; "stop": end the session realistically
    spend_rule: str = "Do not spend money or credits."
    files_description: dict[str, str] = field(default_factory=dict)
    has_inbox: bool = False
    credentials_text: str = ""
    max_page_text: int = 9000


@dataclass
class SessionResult:
    status: str = "running"  # done | gave_up | abandoned | max_steps | budget | error
    steps: int = 0
    site_model: dict = field(default_factory=dict)
    pages: dict = field(default_factory=dict)  # page_key -> review
    trace: list = field(default_factory=list)
    inputs: list = field(default_factory=list)
    captures: list = field(default_factory=list)
    output_reactions: list = field(default_factory=list)
    abandonment: Optional[dict] = None
    final_summary: str = ""
    started: float = field(default_factory=time.time)
    ended: float = 0.0
    waits: list = field(default_factory=list)


class PersonaAgent:
    def __init__(self, persona: Persona, llm: LLMClient, env: BrowserEnv, cfg: AgentConfig, run_dir: Path, log=print):
        self.persona = persona
        self.llm = llm
        self.env = env
        self.cfg = cfg
        self.run_dir = Path(run_dir)
        self.memory = Memory()
        self.result = SessionResult()
        self.log = log
        self._capture_hashes: set[str] = set()
        self._frustration_streak = 0
        self._stuck_count = 0
        self._last_obs_hash = ""
        self._read_full_next = False
        self._system = self._system_prompt()

    # ----------------------------------------------------------- prompting
    def _system_prompt(self) -> str:
        p = self.persona
        return prompts.SYSTEM_TEMPLATE.format(
            profile=p.profile_text(),
            first_name=p.name.split()[0],
            tech_rule=prompts.tech_rule(p.facets.self_efficacy, p.facets.motivation) if not p.baseline else "",
            spend_rule=self.cfg.spend_rule,
            goal=self.cfg.goal,
            heuristics=prompts.heuristics_text(),
            severity=prompts.SEVERITY,
        )

    def _perception_note(self, obs: Observation) -> str:
        p = self.persona
        notes = []
        if p.device == "mobile":
            notes.append("You are on your phone: the screen is narrow and you tap with your thumb.")
        if p.device == "zoom200":
            notes.append("Your browser is zoomed to 200%, so you see only a small part of the page at a time.")
        if p.attention == "skim":
            notes.append("You are skimming: long paragraphs are shown only by their first words (…); use read_page if you really want to read something.")
        if p.attention == "low_vision":
            a = obs.a11y or {}
            if a.get("low_contrast"):
                ex = "; ".join(f'"{x["text"][:30]}"' for x in a["low_contrast"][:4])
                notes.append(f"Some text is too faint for your eyes to read (e.g. {ex}).")
            if a.get("tiny_text"):
                notes.append("Some text is so small that even zoomed in you can't read it.")
            if a.get("small_targets"):
                notes.append("Some controls are tiny and hard for you to hit: " + ", ".join(f'[{x["id"]}]' for x in a["small_targets"][:6]) + ".")
            if a.get("unnamed_controls"):
                notes.append("Some buttons are only little symbols with no words: " + ", ".join(f'[{x["id"]}]' for x in a["unnamed_controls"][:6]) + ".")
        return "\n".join(notes)

    def _extras(self) -> str:
        bits = []
        if self.cfg.files_description:
            bits.append("Files on your computer you could upload: " + "; ".join(f"{k} ({v})" for k, v in self.cfg.files_description.items()))
        if self.cfg.has_inbox:
            bits.append("You can check your e-mail inbox at any time with the read_inbox action.")
        if self.cfg.credentials_text:
            bits.append(self.cfg.credentials_text)
        return "\n".join(bits)

    def _hints(self) -> str:
        hints = []
        if self._stuck_count >= 2:
            hints.append("NOTE: your last few actions did not change anything on screen. Try something different (scroll, another control, go back) - or give up if you really would.")
        if self.result.abandonment and self.cfg.abandon_mode == "note" and self._frustration_streak == self.persona.patience_steps + 1:
            hints.append("NOTE: in real life you might have given up by now. That has been recorded; please continue for the study if you can.")
        left = self.cfg.max_steps - self.result.steps
        if left <= 4 and self.result.captures == [] and "output" in self.cfg.goal.lower():
            hints.append("NOTE: only a few steps left - prioritise reaching and looking at the generated output.")
        return "\n".join(hints)

    def _step_messages(self, obs: Observation, new_page: bool, last_results: list[ActionResult], step: int) -> list[dict]:
        results_txt = "\n".join(
            f"- {r.action.get('type')} {json.dumps({k: v for k, v in r.action.items() if k != 'type'}, ensure_ascii=False)[:160]}: "
            f"{'OK' if r.ok else 'FAILED'} - {r.message}"
            for r in last_results
        ) or "(nothing yet - you just arrived)"
        if obs.events:
            results_txt += "\n" + "\n".join(f"- {e}" for e in obs.events)
        page_text = obs.text
        if self._read_full_next:
            page_text = self.env.observe(attention="full", max_text=20000, with_screenshot=False).text
            self._read_full_next = False
        state = (
            "NEW - you have not reviewed this screen yet, so fill in page_review"
            if new_page
            else "already reviewed (do not repeat page_review; use new_issues for anything new)"
        )
        budget_note = f"; {self.llm.remaining} thinking turns of budget remain" if self.llm.remaining < 12 else ""
        content = prompts.STEP_TEMPLATE.format(
            step=step,
            left=self.cfg.max_steps - step,
            budget_note=budget_note,
            hints=self._hints(),
            journey=self.memory.journey_text(),
            notes=self.memory.notes_text(),
            results=results_txt,
            url=obs.url,
            title=obs.title,
            state=state,
            perception=self._perception_note(obs),
            extras=self._extras(),
            page_text=page_text,
            emotions="|".join(prompts.EMOTIONS),
            q4=prompts.Q4_SCHEMA if step > 1 else "",
            site_model=prompts.SITE_MODEL_SCHEMA if step == 1 else "",
            page_review=prompts.PAGE_REVIEW_SCHEMA if new_page else "",
        )
        user: Any = content
        if self.cfg.vision and obs.screenshot and self.llm.supports_images():
            user = [{"type": "text", "text": content}, image_part(obs.screenshot)]
        return [{"role": "system", "content": self._system}, {"role": "user", "content": user}]

    # ----------------------------------------------------------------- run
    def run(self) -> SessionResult:
        r = self.env.goto(self.cfg.start_url)
        last_results = [r]
        trace_path = self.run_dir / "trace.jsonl"
        for step in range(1, self.cfg.max_steps + 1):
            self.result.steps = step
            self._collect_files()
            obs = self.env.observe(attention=self.persona.attention, max_text=self.cfg.max_page_text, with_screenshot=True)
            shot_path = self.env.save_screenshot(obs.screenshot, f"step_{step:02d}.jpg") if obs.screenshot else None
            new_page = obs.page_key not in self.result.pages
            obs_hash = hashlib.md5((obs.url + obs.text).encode()).hexdigest()
            self._stuck_count = self._stuck_count + 1 if obs_hash == self._last_obs_hash else 0
            self._last_obs_hash = obs_hash
            messages = self._step_messages(obs, new_page, last_results, step)
            t0 = time.time()
            try:
                out, meta = self.llm.chat_json(messages, purpose="step", max_tokens=5000)
            except BudgetExceeded:
                self.result.status = "budget"
                break
            except LLMError as e:
                self.log(f"  step {step}: LLM error {e}")
                self.result.trace.append({"step": step, "error": str(e), "url": obs.url})
                last_results = [ActionResult({"type": "none"}, False, "(your previous turn was lost; please look again)")]
                if len([t for t in self.result.trace if "error" in t]) >= 3:
                    self.result.status = "error"
                    break
                continue
            if not isinstance(out, dict):
                out = {"actions": []}
            llm_s = time.time() - t0
            self._record_understanding(step, obs, out, new_page, shot_path)
            actions = [a for a in (out.get("actions") or []) if isinstance(a, dict)][: self.cfg.max_actions_per_step]
            if out.get("output_present"):
                self._capture("auto: " + (obs.headings[0] if obs.headings else obs.title))
                if out.get("output_reaction"):
                    self.result.output_reactions.append({"step": step, "url": obs.url, "reaction": out["output_reaction"]})
            results: list[ActionResult] = []
            terminal = None
            for a in actions:
                kind = str(a.get("type", "")).lower()
                if kind in TERMINAL:
                    terminal = a
                    results.append(ActionResult(a, True, "ending session"))
                    break
                if kind == "read_page":
                    self._read_full_next = True
                    results.append(ActionResult(a, True, "you will read the full page next"))
                    continue
                if kind == "flip_through":
                    caps = self.env.flip_through(int(a.get("id", -1)), int(a.get("max_pages", 40)), label=obs.headings[0] if obs.headings else "")
                    for c in caps:
                        self._register_capture(c)
                    results.append(ActionResult(a, bool(caps), f"you paged through {len(caps)} pages and looked at each one" if caps else "that control did not page through anything"))
                    continue
                if kind == "capture_output":
                    self._capture(a.get("label", "manual"))
                    results.append(ActionResult(a, True, "you looked closely at this output"))
                    continue
                res = self.env.execute(a)
                results.append(res)
                self._record_input(a, res)
                self._collect_files()
                if kind in ("wait", "wait_for_change") and res.data.get("waited_s"):
                    self.result.waits.append({"step": step, "seconds": res.data["waited_s"], "timeout": res.data.get("timeout", False), "url": obs.url})
                if kind == "read_inbox" and res.data.get("code"):
                    self.memory.note(f"code from e-mail: {res.data['code']}")
                if not res.ok or res.navigated:
                    break
            outcome = "; ".join(f"{'ok' if x.ok else 'FAILED'}: {x.message[:90]}" for x in results) or "no action"
            self.memory.add(
                StepMemory(
                    step=step,
                    page=(obs.headings[0][:40] if obs.headings else obs.title[:40]) or obs.url[-40:],
                    thought=str(out.get("think_aloud", "")),
                    emotion=str(out.get("emotion", "")),
                    actions=[_fmt_action(a, obs) for a in actions] or ["(no action)"],
                    outcome=outcome,
                )
            )
            if out.get("memory_note"):
                self.memory.note(str(out["memory_note"]))
            record = {
                "step": step,
                "url": obs.url,
                "title": obs.title,
                "page_key": obs.page_key,
                "new_page": new_page,
                "screenshot": shot_path,
                "llm_seconds": round(llm_s, 1),
                "model": meta.get("model"),
                "output": out,
                "results": [x.to_json() for x in results],
                "a11y": obs.a11y,
                "events": obs.events,
                "page_text": obs.text,
            }
            self.result.trace.append(record)
            with trace_path.open("a") as f:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")
            self.log(
                f"  step {step:>2} [{obs.page_key[:60]}] {out.get('emotion', '?')}/{out.get('valence', '?')} "
                f"-> {', '.join(_fmt_action(a, obs) for a in actions)[:140]}"
            )
            self._update_affect(step, obs, out, results)
            if self.result.status == "abandoned":
                break
            if terminal or str(out.get("status", "")).lower() in ("done", "give_up"):
                kind = (terminal or {}).get("type") or str(out.get("status")).lower()
                self.result.status = "done" if kind == "done" else "gave_up"
                self.result.final_summary = str((terminal or {}).get("summary") or (terminal or {}).get("reason") or out.get("plan", ""))
                break
            last_results = results or [ActionResult({"type": "none"}, True, "you did nothing")]
        else:
            self.result.status = "max_steps"
        if self.result.status == "running":
            self.result.status = "max_steps"
        self._collect_files()
        self.result.ended = time.time()
        return self.result

    def _collect_files(self) -> None:
        try:
            for cap in self.env.collect_file_outputs():
                self._register_capture(cap)
        except Exception as e:  # file handling must never kill a session
            self.log(f"  file capture failed: {e}")

    # --------------------------------------------------------- bookkeeping
    def _clean_issues(self, issues: Any, obs: Observation) -> list[dict]:
        out = []
        page_text = obs.text + "\n" + obs.full_text + "\n" + obs.title
        for i in issues if isinstance(issues, list) else []:
            if not isinstance(i, dict):
                continue
            if not i.get("title"):
                basis = str(i.get("why_it_matters_to_me") or i.get("evidence") or i.get("fix") or "").strip()
                if not basis:
                    continue
                i["title"] = basis.split(". ")[0][:90]
            i["evidence_check"] = verify_evidence(str(i.get("evidence", "")), page_text)
            out.append(i)
        return out

    def _record_understanding(self, step: int, obs: Observation, out: dict, new_page: bool, shot: Optional[str]) -> None:
        if step == 1 and isinstance(out.get("site_model"), dict):
            self.result.site_model = out["site_model"]
        elif isinstance(out.get("site_model"), dict) and out["site_model"]:
            self.result.site_model.update({k: v for k, v in out["site_model"].items() if v})
        review = out.get("page_review") if new_page else None
        if isinstance(review, dict):
            review["issues"] = self._clean_issues(review.get("issues"), obs)
        if new_page:
            self.result.pages[obs.page_key] = {
                "page_key": obs.page_key,
                "url": obs.url,
                "title": obs.title,
                "first_step": step,
                "screenshot": shot,
                "observation": out.get("observation", ""),
                "think_aloud": out.get("think_aloud", ""),
                "emotion": out.get("emotion", ""),
                "valence": out.get("valence"),
                "review": review if isinstance(review, dict) else {},
                "later_issues": [],
                "a11y": _a11y_summary(obs.a11y),
                "visits": 1,
            }
        else:
            pg = self.result.pages.get(obs.page_key)
            if pg:
                pg["visits"] += 1
        extra = self._clean_issues(out.get("new_issues"), obs)
        if extra:
            tgt = self.result.pages.get(obs.page_key)
            if tgt is not None:
                for i in extra:
                    i["step"] = step
                tgt["later_issues"].extend(extra)
        pr = review if isinstance(review, dict) else {}
        if pr.get("would_abandon_here") and not self.result.abandonment:
            self.result.abandonment = {"step": step, "page": obs.page_key, "reason": pr.get("abandon_reason", ""), "source": "self-report"}
            if self.cfg.abandon_mode == "stop":
                self.result.status = "abandoned"

    def _update_affect(self, step: int, obs: Observation, out: dict, results: list[ActionResult]) -> None:
        try:
            val = float(out.get("valence", 0))
        except (TypeError, ValueError):
            val = 0.0
        failed = any(not r.ok for r in results)
        if val <= -1 or failed or self._stuck_count >= 2:
            self._frustration_streak += 1
        else:
            self._frustration_streak = 0
        if self._frustration_streak > self.persona.patience_steps and not self.result.abandonment:
            self.result.abandonment = {
                "step": step,
                "page": obs.page_key,
                "reason": f"{self._frustration_streak} consecutive frustrating steps exceeded patience ({self.persona.patience_steps})",
                "source": "patience model",
            }
            if self.cfg.abandon_mode == "stop":
                self.result.status = "abandoned"

    def _record_input(self, a: dict, res: ActionResult) -> None:
        kind = str(a.get("type", "")).lower()
        info = self.env._info(a.get("id")) if a.get("id") is not None else None
        field_name = (info or {}).get("name") or (info or {}).get("placeholder") or f"[{a.get('id')}]"
        if kind in INPUT_ACTIONS and res.ok:
            value = a.get("text") or a.get("option") or a.get("value") or a.get("file")
            if (info or {}).get("type") == "password":
                value = "(password)"
            self.result.inputs.append({"field": field_name, "action": kind, "value": value, **({"truncated_to": res.data["truncated_to"]} if res.data.get("truncated_to") else {})})
        elif kind == "click" and res.ok and info and info.get("role") in ("radio", "checkbox"):
            self.result.inputs.append({"field": field_name, "action": "choose", "value": info.get("value") or field_name})

    def _capture(self, label: str) -> None:
        try:
            cap = self.env.capture_output(label=label)
        except Exception as e:  # capture must never kill a session
            self.log(f"  capture failed: {e}")
            return
        self._register_capture(cap)

    def _register_capture(self, cap: dict) -> None:
        h = hashlib.md5((cap.get("dedupe_key") or cap["text"]).encode()).hexdigest()
        if h in self._capture_hashes:
            return
        self._capture_hashes.add(h)
        self.result.captures.append(cap)


_QUOTE_RE = re.compile(r"“([^”]{4,200})”|\"([^\"]{4,200})\"|‘([^’]{4,200})’(?![a-z])|(?<![A-Za-z])'([^']{4,200})'(?![A-Za-z])")


def _norm(s: str) -> str:
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def verify_evidence(evidence: str, page_text: str) -> dict:
    """Check that quoted evidence actually occurs on the page (guards against paraphrased or 'corrected' quotes)."""
    quotes = [next(g for g in m if g).strip(" .,;:…") for m in _QUOTE_RE.findall(evidence)]
    quotes = [q for q in quotes if len(q) >= 4]
    if not quotes:
        return {"quotes": 0, "verified": None}
    hay = _norm(page_text)
    found = sum(1 for q in quotes if _norm(q) in hay)
    return {"quotes": len(quotes), "found": found, "verified": found == len(quotes)}


def _fmt_action(a: dict, obs: Optional[Observation] = None) -> str:
    kind = a.get("type", "?")
    el = ""
    if obs is not None and a.get("id") is not None:
        try:
            info = obs.elements.get(int(a["id"]))
        except (TypeError, ValueError):
            info = None
        if info:
            el = f' "{(info.get("name") or info.get("placeholder") or "")[:40]}"'
    if kind == "type":
        t = str(a.get("text", ""))
        return f"type[{a.get('id')}]{el} '{t[:40]}{'…' if len(t) > 40 else ''}'"
    if kind in ("click", "select", "set_range", "upload", "flip_through"):
        extra = a.get("option") or a.get("value") or a.get("file") or ""
        return f"{kind}[{a.get('id')}]{el}{' ' + str(extra) if extra else ''}"
    if kind in ("done", "give_up"):
        return kind
    return kind + (f" {a.get('direction')}" if a.get("direction") else "")


def _a11y_summary(a: dict) -> dict:
    a = a or {}
    return {
        "images_missing_alt": len(a.get("images_missing_alt", [])),
        "unlabeled_fields": len(a.get("unlabeled_fields", [])),
        "placeholder_only_fields": len(a.get("placeholder_only_fields", [])),
        "unnamed_controls": len(a.get("unnamed_controls", [])),
        "small_targets": len(a.get("small_targets", [])),
        "low_contrast_texts": len(a.get("low_contrast", [])),
        "tiny_texts": len(a.get("tiny_text", [])),
        "examples": {
            "low_contrast": a.get("low_contrast", [])[:3],
            "unnamed_controls": a.get("unnamed_controls", [])[:3],
            "images_missing_alt": a.get("images_missing_alt", [])[:3],
            "placeholder_only_fields": a.get("placeholder_only_fields", [])[:3],
        },
    }
