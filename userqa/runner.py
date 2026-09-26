"""End-to-end orchestration of one simulated-user session."""
from __future__ import annotations

import json
import os
import re
import time
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

import yaml

from .agent.loop import INPUT_ACTIONS, AgentConfig, PersonaAgent
from .browser.env import BrowserEnv, SafetyPolicy
from .evaluation.fidelity import audit_fidelity
from .evaluation.issues import cluster_issues, flatten_issues
from .evaluation.output_assessor import OutputAssessor
from .evaluation.questionnaires import journey_digest, run_debrief
from .llm import DEFAULT_MODEL, BudgetExceeded, LLMClient
from .personas.schema import Persona, load_persona

# Experiment suites run a frozen copy of the package; USERQA_ROOT keeps .env, sites and secrets in the workspace.
ROOT = Path(os.environ.get("USERQA_ROOT") or Path(__file__).resolve().parent.parent)


def load_env_file(path: Path = ROOT / ".env") -> None:
    if path.exists():
        for line in path.read_text().splitlines():
            if "=" in line and not line.strip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def load_site(ref: str) -> dict:
    p = Path(ref)
    if not p.exists():
        p = ROOT / "experiments" / "sites" / f"{ref}.yaml"
    return yaml.safe_load(p.read_text())


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]


def previous_visit_note(prev: Path) -> str:
    """What a returning user remembers of their earlier session: how it ended and what they wanted changed."""
    prev = Path(prev)
    s = json.loads((prev / "session.json").read_text())
    a = json.loads((prev / "output_assessment.json").read_text()) if (prev / "output_assessment.json").exists() else {}
    bits = []
    if s.get("final_summary"):
        bits.append("How your last visit ended: " + str(s["final_summary"]))
    if a.get("overall_reaction"):
        bits.append("What you thought of what the site made for you: " + str(a["overall_reaction"]))
    if a.get("top_changes"):
        bits.append("What you wanted changed: " + "; ".join(str(x) for x in a["top_changes"][:4]))
    return "\n".join(bits)


def run_session(
    site: dict,
    persona: Persona,
    out_dir: Path,
    model: str = DEFAULT_MODEL,
    fallbacks: Optional[list[str]] = None,
    max_steps: Optional[int] = None,
    max_llm_calls: Optional[int] = None,
    headless: bool = False,
    vision: bool = True,
    abandon_mode: str = "note",
    temperature: float = 0.7,
    skip_fidelity: bool = False,
    previous_run: Optional[Path] = None,
    log=print,
) -> Path:
    load_env_file()
    previous_run = previous_run or (ROOT / site["previous_run"] if site.get("previous_run") else None)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    run_dir = Path(out_dir) / f"{stamp}_{_slug(site.get('name', 'site'))}_{persona.id}"
    run_dir.mkdir(parents=True, exist_ok=True)
    persona.dump(run_dir / "persona.yaml")
    llm = LLMClient(
        model=model,
        fallbacks=fallbacks,
        max_calls=max_llm_calls or int(site.get("max_llm_calls", 60)),
        log_path=run_dir / "llm_calls.jsonl",
        temperature=temperature,
    )

    # --- identity: a real inbox for sites with e-mail verification
    inbox = None
    credentials_text = site.get("credentials_text", "")
    if site.get("inbox") == "mailtm":
        from .tools.inbox import Inbox

        box_file = ROOT / str(site.get("inbox_file", ".secrets/mailbox_{persona}.json")).format(persona=persona.id, site=_slug(site.get("name", "")))
        inbox = Inbox.load_or_create(box_file, prefix=persona.name.split()[0].lower())
        inbox.mark_all_seen()
        persona.domain_context["email"] = inbox.mailbox.address
        credentials_text = (credentials_text + "\n" if credentials_text else "") + (
            f"Your e-mail address is {inbox.mailbox.address} (use it to sign up or log in; you can read its inbox with read_inbox)."
        )
    if site.get("credentials"):
        c = site["credentials"]
        credentials_text = (credentials_text + "\n" if credentials_text else "") + "Your account for this website: " + ", ".join(f"{k}: {v}" for k, v in c.items())
        if c.get("email"):
            persona.domain_context["email"] = c["email"]

    assets = {k: (ROOT / v["path"]) for k, v in (site.get("assets") or {}).items()}
    files_description = {k: v.get("description", "") for k, v in (site.get("assets") or {}).items()}
    safety = SafetyPolicy(
        allowed_click_patterns=site.get("allow_click_patterns", []),
        allowed_domains=site.get("allowed_domains", []),
    )
    storage = site.get("storage_state")
    storage_path = (ROOT / storage.format(persona=persona.id)) if storage else None
    env = BrowserEnv(
        run_dir=run_dir,
        device=persona.device,
        headless=headless,
        storage_state=storage_path if storage_path and storage_path.exists() and site.get("reuse_session", False) else None,
        safety=safety,
        assets=assets,
        inbox=inbox,
        locale=persona.locale,
        auto_captcha=bool(site.get("auto_captcha", True)),
        timezone_id=site.get("timezone_id"),
    )
    goal = site["goal"].strip()
    if previous_run:
        goal += "\n\nYOU HAVE USED THIS SITE BEFORE. What you remember from last time:\n" + previous_visit_note(previous_run)
    cfg = AgentConfig(
        start_url=site["url"],
        goal=goal,
        max_steps=max_steps or int(site.get("max_steps", 30)),
        vision=vision,
        abandon_mode=abandon_mode,
        spend_rule=site.get("spend_rule", "Do not spend any money or credits."),
        files_description=files_description,
        has_inbox=inbox is not None,
        credentials_text=credentials_text,
    )
    config_record = {
        "site": {k: v for k, v in site.items() if k not in ("credentials",)},
        "persona": persona.id,
        "model": model,
        "fallbacks": llm.fallbacks,
        "max_steps": cfg.max_steps,
        "max_llm_calls": llm.max_calls,
        "vision": vision,
        "abandon_mode": abandon_mode,
        "temperature": temperature,
        "device": persona.device,
        "attention": persona.attention,
        "started_utc": stamp,
        "inbox": inbox.mailbox.address if inbox else None,
        "previous_run": str(previous_run) if previous_run else None,
    }
    (run_dir / "config.json").write_text(json.dumps(config_record, indent=2))
    log(f"[run] {run_dir.name}: persona={persona.id} model={model} url={site['url']}")
    t0 = time.time()
    env.start()
    agent = PersonaAgent(persona, llm, env, cfg, run_dir, log=log)
    session = None
    try:
        session = agent.run()
    finally:
        try:
            if storage_path and site.get("save_session", False):
                env.save_storage_state(storage_path)
        except Exception:
            pass
        env_stats = {"http_errors": env.http_errors[-50:], "console_errors": env.console_errors[-30:], "page_loads": env.page_loads,
                     "captcha": env.challenge_log, "files": env.files}
        env.close()
    session_json = {
        "status": session.status,
        "steps": session.steps,
        "site_model": session.site_model,
        "pages": session.pages,
        "inputs": session.inputs,
        "captures": [{k: v for k, v in c.items() if k != "text"} | {"text_chars": len(c.get("text", ""))} for c in session.captures],
        "output_reactions": session.output_reactions,
        "abandonment": session.abandonment,
        "final_summary": session.final_summary,
        "waits": session.waits,
        "duration_s": round(session.ended - session.started, 1),
        "env": env_stats,
    }
    (run_dir / "session.json").write_text(json.dumps(session_json, indent=2, ensure_ascii=False))
    log(f"[run] session ended: {session.status} after {session.steps} steps, {len(session.pages)} pages, {len(session.captures)} output captures")

    # --- post-session evaluation (each stage tolerates budget exhaustion)
    extra_budget = 8
    llm.max_calls = max(llm.max_calls, llm.usage.calls + extra_budget)
    assessment: dict[str, Any] = {}
    try:
        assessment = OutputAssessor(llm, run_dir, vision=vision).assess(persona, session.inputs, session.captures, session.output_reactions)
    except BudgetExceeded:
        assessment = {"skipped": True, "reason": "LLM budget exhausted"}
    (run_dir / "output_assessment.json").write_text(json.dumps(assessment, indent=2, ensure_ascii=False))
    journey = journey_digest(session.trace, session.pages, session.waits)
    output_summary = ""
    if assessment and not assessment.get("skipped"):
        output_summary = json.dumps(
            {k: assessment.get(k) for k in ("overall_reaction", "criteria", "top_changes", "keepsake_worthiness")}, ensure_ascii=False
        )
    try:
        debrief = run_debrief(llm, persona, journey, output_summary)
    except BudgetExceeded:
        debrief = {"error": "LLM budget exhausted"}
    (run_dir / "debrief.json").write_text(json.dumps(debrief, indent=2, ensure_ascii=False))
    fidelity = {"skipped": True}
    if not skip_fidelity:
        try:
            fidelity = audit_fidelity(llm, persona, journey)
        except BudgetExceeded:
            fidelity = {"skipped": True, "reason": "LLM budget exhausted"}
    (run_dir / "fidelity.json").write_text(json.dumps(fidelity, indent=2, ensure_ascii=False))

    summary = build_summary(run_dir, persona, session_json, assessment, debrief, fidelity, llm, time.time() - t0, model)
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    from .report.render import render_report

    render_report(run_dir)
    log(f"[run] report: {run_dir / 'report.html'}  (LLM calls: {llm.usage.calls}, failed: {llm.usage.failed_calls})")
    return run_dir


def backfill_input_context(inputs: list[dict], trace: list[dict]) -> list[dict]:
    """Add the step, screen and element id to inputs of runs recorded before they were logged, from the trace.

    Every successful type/select/set_range/upload action in the trace produced exactly one input, in order."""
    if not inputs or any("id" in i for i in inputs):
        return inputs
    acts = [(t["step"], t.get("page_key"), r["action"].get("id")) for t in trace if "error" not in t
            for r in t.get("results", []) if r.get("ok") and str(r["action"].get("type", "")).lower() in INPUT_ACTIONS]
    typed = [i for i in inputs if i.get("action") in INPUT_ACTIONS]
    if len(acts) != len(typed):
        return inputs
    for i, (step, page, element) in zip(typed, acts):
        i.update(step=step, page=page, id=element)
    return inputs


def reassess_run(run_dir: Path, with_debrief: bool = False, log=print, vision: Optional[bool] = None, variant: str = "") -> Path:
    """Re-run the post-session output assessment (and optionally the debrief) of a finished run.

    Used when the assessment stage changes after sessions were collected: the browsing session itself
    is not repeated, so live sites are not visited (or charged) again. With ``variant`` (e.g. a paired
    no-vision ablation) the result goes to output_assessment.<variant>.json and the run is otherwise untouched.
    """
    load_env_file()
    run_dir = Path(run_dir)
    cfg = json.loads((run_dir / "config.json").read_text())
    session = json.loads((run_dir / "session.json").read_text())
    persona = load_persona(str(run_dir / "persona.yaml"))
    trace = [json.loads(ln) for ln in (run_dir / "trace.jsonl").read_text().splitlines()] if (run_dir / "trace.jsonl").exists() else []
    backfill_input_context(session.get("inputs") or [], trace)
    captures = []
    for c in session.get("captures") or []:
        t = run_dir / c.get("dir", "") / "text.txt"
        captures.append({**c, "text": t.read_text() if t.exists() else ""})
    llm = LLMClient(model=cfg.get("model", DEFAULT_MODEL), fallbacks=cfg.get("fallbacks"), max_calls=40,
                    log_path=run_dir / "llm_calls.jsonl", temperature=float(cfg.get("temperature", 0.7)))
    vision = bool(cfg.get("vision", True)) if vision is None else vision
    if variant:
        assessment = OutputAssessor(llm, run_dir, vision=vision).assess(persona, session.get("inputs") or [], captures, session.get("output_reactions") or [])
        assessment["variant"] = {"name": variant, "vision": vision, "llm_usage": llm.usage.to_json()}
        (run_dir / f"output_assessment.{variant}.json").write_text(json.dumps(assessment, indent=2, ensure_ascii=False))
        log(f"[reassess:{variant}] {run_dir.name}: {len(assessment.get('parts') or [])} parts, LLM calls {llm.usage.calls}")
        return run_dir
    for name in ("output_assessment.json", "debrief.json", "summary.json"):
        if (run_dir / name).exists() and (name != "debrief.json" or with_debrief):
            (run_dir / name).with_suffix(".prev.json").write_text((run_dir / name).read_text())
    assessment = OutputAssessor(llm, run_dir, vision=vision).assess(persona, session.get("inputs") or [], captures, session.get("output_reactions") or [])
    (run_dir / "output_assessment.json").write_text(json.dumps(assessment, indent=2, ensure_ascii=False))
    debrief = json.loads((run_dir / "debrief.json").read_text()) if (run_dir / "debrief.json").exists() else {}
    if with_debrief:
        output_summary = json.dumps({k: assessment.get(k) for k in ("overall_reaction", "criteria", "top_changes", "keepsake_worthiness")}, ensure_ascii=False)
        debrief = run_debrief(llm, persona, journey_digest(trace, session.get("pages") or {}, session.get("waits") or []), output_summary)
        (run_dir / "debrief.json").write_text(json.dumps(debrief, indent=2, ensure_ascii=False))
    fidelity = json.loads((run_dir / "fidelity.json").read_text()) if (run_dir / "fidelity.json").exists() else {}
    old = json.loads((run_dir / "summary.json").read_text()) if (run_dir / "summary.json").exists() else {}
    summary = build_summary(run_dir, persona, session, assessment, debrief, fidelity, llm, old.get("wall_seconds", 0), cfg.get("model", DEFAULT_MODEL))
    if old.get("llm_usage"):
        summary["llm_usage"] = old["llm_usage"]
        summary["llm_usage_reassess"] = llm.usage.to_json()
    summary["reassessed"] = True
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False))
    from .report.render import render_report

    render_report(run_dir)
    log(f"[reassess] {run_dir.name}: {len(assessment.get('parts') or [])} parts, superseded {assessment.get('superseded_captures')}, LLM calls {llm.usage.calls}")
    return run_dir


def build_summary(run_dir, persona, session, assessment, debrief, fidelity, llm, seconds, model) -> dict:
    issues = flatten_issues(session["pages"])
    unique = cluster_issues(issues)
    checks = [i.get("evidence_check") or {} for i in issues]
    quoted = [c for c in checks if c.get("quotes")]
    sev = [int(i.get("severity", 0) or 0) for i in issues if str(i.get("severity", "")).strip().isdigit()]
    valences = []
    for line in (Path(run_dir) / "trace.jsonl").read_text().splitlines() if (Path(run_dir) / "trace.jsonl").exists() else []:
        try:
            v = json.loads(line).get("output", {}).get("valence")
            valences.append(float(v))
        except (TypeError, ValueError, json.JSONDecodeError):
            pass
    crit = (assessment or {}).get("criteria") or {}
    crit_scores = {}
    for k, v in crit.items():
        s = v.get("score") if isinstance(v, dict) else v
        try:
            crit_scores[k] = float(s)
        except (TypeError, ValueError):
            crit_scores[k] = None
    return {
        "run": Path(run_dir).name,
        "persona": persona.id,
        "persona_name": persona.name,
        "model": model,
        "status": session["status"],
        "steps": session["steps"],
        "pages_reviewed": len(session["pages"]),
        "issues": len(issues),
        "unique_issues": len(unique),
        "evidence_quotes_verified": round(sum(1 for c in quoted if c.get("verified")) / len(quoted), 3) if quoted else None,
        "issues_by_severity": {str(s): sev.count(s) for s in range(5)},
        "issues_by_code": _count([str(i.get("code", "?")).split()[0].upper() for i in issues]),
        "reached_output": bool(session["captures"]),
        "output_parts": len((assessment or {}).get("parts") or []),
        "output_criteria": crit_scores,
        "keepsake_worthiness": (assessment or {}).get("keepsake_worthiness"),
        "sus": (debrief.get("sus_score") or {}).get("score") if isinstance(debrief, dict) else None,
        "sus_grade": (debrief.get("sus_score") or {}).get("grade") if isinstance(debrief, dict) else None,
        "sus_consistency_flag": (debrief.get("sus_score") or {}).get("consistency_flag") if isinstance(debrief, dict) else None,
        "ueq_s": debrief.get("ueq_s_score") if isinstance(debrief, dict) else None,
        "nps": debrief.get("nps") if isinstance(debrief, dict) else None,
        "mean_valence": round(sum(valences) / len(valences), 2) if valences else None,
        "min_valence": min(valences) if valences else None,
        "abandonment": session.get("abandonment"),
        "waits": session.get("waits"),
        "fidelity": {k: (v.get("score") if isinstance(v, dict) else v) for k, v in (fidelity or {}).items() if k != "facet_consistency"},
        "llm_usage": llm.usage.to_json(),
        "wall_seconds": round(seconds, 1),
    }


def _count(xs: list[str]) -> dict:
    d: dict[str, int] = {}
    for x in xs:
        d[x] = d.get(x, 0) + 1
    return dict(sorted(d.items(), key=lambda kv: -kv[1]))
