"""Render a session directory into ``report.html`` and ``report.md``."""
from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

from ..agent.prompts import HEURISTICS
from ..evaluation.issues import cluster_issues, flatten_issues
from ..evaluation.questionnaires import INTERVIEW, SUS_ITEMS, UEQS_ITEMS

TEMPLATES = Path(__file__).parent / "templates"
SEV_LABEL = {0: "none", 1: "cosmetic", 2: "minor", 3: "major", 4: "catastrophic"}


def _load(run_dir: Path, name: str, default: Any = None) -> Any:
    p = run_dir / name
    if not p.exists():
        return default
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError:
        return default


def _trace(run_dir: Path) -> list[dict]:
    p = run_dir / "trace.jsonl"
    if not p.exists():
        return []
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()]


def _sev(i: dict) -> int:
    try:
        return int(i.get("severity", 0))
    except (TypeError, ValueError):
        return 0


def valence_svg(trace: list[dict], width: int = 900, height: int = 190) -> str:
    pts = []
    for t in trace:
        o = t.get("output") or {}
        try:
            pts.append((t["step"], float(o.get("valence", 0)), str(o.get("emotion", "")), (t.get("title") or "")[:30]))
        except (TypeError, ValueError):
            continue
    if not pts:
        return ""
    n = max(p[0] for p in pts)
    pad_l, pad_r, pad_t, pad_b = 40, 20, 18, 30
    w, h = width - pad_l - pad_r, height - pad_t - pad_b
    x = lambda s: pad_l + (w * (s - 1) / max(1, n - 1))
    y = lambda v: pad_t + h * (2 - v) / 4
    grid = "".join(
        f'<line x1="{pad_l}" x2="{width - pad_r}" y1="{y(v)}" y2="{y(v)}" stroke="#e5e7eb"/><text x="6" y="{y(v) + 4}" font-size="11" fill="#6b7280">{v:+d}</text>'
        for v in (-2, -1, 0, 1, 2)
    )
    path = " ".join(f"{'M' if i == 0 else 'L'}{x(s):.1f},{y(v):.1f}" for i, (s, v, _, _) in enumerate(pts))
    dots = "".join(
        f'<circle cx="{x(s):.1f}" cy="{y(v):.1f}" r="4.5" fill="{"#16a34a" if v > 0 else "#dc2626" if v < 0 else "#6b7280"}"><title>Step {s}: {html.escape(e)} ({v:+.0f}) - {html.escape(t)}</title></circle>'
        f'<text x="{x(s):.1f}" y="{height - 10}" font-size="10" text-anchor="middle" fill="#6b7280">{s}</text>'
        for s, v, e, t in pts
    )
    return f'<svg viewBox="0 0 {width} {height}" width="100%" role="img" aria-label="Emotional valence per step">{grid}<path d="{path}" fill="none" stroke="#6366f1" stroke-width="2.5"/>{dots}</svg>'


def criteria_rows(assessment: dict) -> list[dict]:
    rows = []
    for k, v in (assessment.get("criteria") or {}).items():
        if isinstance(v, dict):
            s = v.get("score")
            try:
                sf = float(s)
            except (TypeError, ValueError):
                sf = None
            rows.append({"name": k.replace("_", " "), "score": s, "pct": (sf / 5 * 100) if sf else 0, "evidence": v.get("evidence") or v.get("rationale") or ""})
    return rows


def render_report(run_dir: Path) -> None:
    run_dir = Path(run_dir)
    summary = _load(run_dir, "summary.json", {})
    session = _load(run_dir, "session.json", {})
    config = _load(run_dir, "config.json", {})
    assessment = _load(run_dir, "output_assessment.json", {}) or {}
    debrief = _load(run_dir, "debrief.json", {}) or {}
    fidelity = _load(run_dir, "fidelity.json", {}) or {}
    persona = yaml.safe_load((run_dir / "persona.yaml").read_text()) if (run_dir / "persona.yaml").exists() else {}
    trace = _trace(run_dir)
    pages = sorted((session.get("pages") or {}).values(), key=lambda p: p.get("first_step", 0))
    for p in pages:
        rv = p.get("review") or {}
        issues = [i for i in (rv.get("issues") or []) if isinstance(i, dict)] + [dict(i, later=True) for i in (p.get("later_issues") or []) if isinstance(i, dict)]
        p["issues_sorted"] = sorted(issues, key=lambda i: -_sev(i))
    top_issues = cluster_issues(flatten_issues(session.get("pages") or {}))[:15]
    images = {im["ref"]: im for im in assessment.get("images", [])}
    sus_items = []
    for x in debrief.get("sus", []) if isinstance(debrief.get("sus"), list) else []:
        try:
            idx = int(x.get("item")) - 1
            sus_items.append({"q": SUS_ITEMS[idx], "rating": x.get("rating"), "reason": x.get("reason", "")})
        except (TypeError, ValueError, IndexError):
            continue
    ueq_items = []
    for (a, b, scale), x in zip(UEQS_ITEMS, debrief.get("ueq_s", []) if isinstance(debrief.get("ueq_s"), list) else []):
        ueq_items.append({"left": a, "right": b, "scale": scale, "rating": x.get("rating") if isinstance(x, dict) else x})
    interview = [(q, (debrief.get("interview") or {}).get(k, "")) for k, q in INTERVIEW]
    ctx = dict(
        summary=summary, session=session, config=config, assessment=assessment, debrief=debrief, fidelity=fidelity, persona=persona,
        trace=trace, pages=pages, top_issues=top_issues, images=images, sus_items=sus_items, ueq_items=ueq_items, interview=interview,
        valence_svg=valence_svg(trace), criteria=criteria_rows(assessment), heuristics=HEURISTICS, sev_label=SEV_LABEL,
    )
    env = Environment(loader=FileSystemLoader(str(TEMPLATES)), autoescape=select_autoescape(["html"]))
    env.filters["sev"] = _sev
    env.filters["tojson_pretty"] = lambda v: json.dumps(v, indent=2, ensure_ascii=False)
    (run_dir / "report.html").write_text(env.get_template("report.html.j2").render(**ctx))
    (run_dir / "report.md").write_text(render_markdown(ctx))


def _md(s: Any) -> str:
    return str(s or "").replace("\n", " ").replace("|", "\\|").strip()


def render_markdown(c: dict) -> str:
    s, p, a, d = c["summary"], c["persona"], c["assessment"], c["debrief"]
    sm = (c["session"] or {}).get("site_model") or {}
    L = []
    L.append(f"# UserQA report: {p.get('name', '')} on {c['config'].get('site', {}).get('url', '')}")
    L.append("")
    L.append(f"*Persona:* **{p.get('name')}** ({p.get('age')}) - {p.get('tagline')}  ")
    L.append(f"*Model:* `{s.get('model')}` | *Status:* **{s.get('status')}** after {s.get('steps')} steps | *Pages reviewed:* {s.get('pages_reviewed')} | *Issues:* {s.get('issues')} | *LLM calls:* {(s.get('llm_usage') or {}).get('calls')} | *Wall time:* {s.get('wall_seconds')} s")
    L.append("")
    L.append("## What the agent understood the website to be")
    for k in ("what_it_is", "who_it_is_for", "value_proposition", "pricing_model", "fit_for_me"):
        if sm.get(k):
            L.append(f"- **{k.replace('_', ' ')}:** {_md(sm[k])}")
    if sm.get("main_tasks"):
        L.append(f"- **main tasks:** {', '.join(map(str, sm['main_tasks']))}")
    L.append("")
    L.append("## Scores")
    L.append(f"- SUS: **{s.get('sus')}** (grade {s.get('sus_grade')}; 68 = industry average){' - inconsistent responding flagged' if s.get('sus_consistency_flag') else ''}")
    u = s.get("ueq_s") or {}
    if u:
        L.append(f"- UEQ-S: pragmatic {u.get('pragmatic')}, hedonic {u.get('hedonic')} (range -3..+3)")
    L.append(f"- Likelihood to recommend (0-10): {s.get('nps')}")
    if s.get("keepsake_worthiness") is not None:
        L.append(f"- Output keepsake-worthiness (1-5): {s.get('keepsake_worthiness')}")
    if d.get("one_line_verdict"):
        L.append(f"- Verdict: *\"{_md(d['one_line_verdict'])}\"*")
    if s.get("abandonment"):
        ab = s["abandonment"]
        L.append(f"- Would have abandoned at step {ab.get('step')} ({_md(ab.get('page'))}): {_md(ab.get('reason'))} [{ab.get('source')}]")
    L.append("")
    L.append("## Top issues")
    L.append("| Sev | Code | Page | Issue | Evidence | Suggested fix |")
    L.append("|---|---|---|---|---|---|")
    for i in c["top_issues"]:
        where = ", ".join(i.get("pages") or [i.get("page") or ""]) + (f" (x{i['occurrences']})" if i.get("occurrences", 1) > 1 else "")
        L.append(f"| {i.get('max_severity', i.get('severity'))} | {_md(i.get('code'))} | {_md(where)} | {_md(i.get('title'))} | {_md(i.get('evidence'))[:160]} | {_md(i.get('fix'))[:200]} |")
    L.append("")
    L.append("## Page-by-page")
    for pg in c["pages"]:
        rv = pg.get("review") or {}
        L.append(f"### {rv.get('page_name') or pg.get('title')}  (step {pg.get('first_step')})")
        L.append(f"`{pg.get('url')}`")
        L.append("")
        if pg.get("screenshot"):
            L.append(f"![screenshot]({pg['screenshot']})")
        if rv.get("purpose"):
            L.append(f"- **Purpose:** {_md(rv['purpose'])}")
        L.append(f"- **What's happening:** {_md(rv.get('what_is_happening') or pg.get('observation'))}")
        L.append(f"- **First impression ({p.get('name', '').split(' ')[0]}):** \"{_md(rv.get('first_impression') or pg.get('think_aloud'))}\"")
        wt = rv.get("walkthrough") or {}
        if wt:
            L.append(f"- **Cognitive walkthrough:** Q1 {_md(wt.get('q1_would_try'))} / Q2 {_md(wt.get('q2_notice_control'))} / Q3 {_md(wt.get('q3_label_matches_goal'))}")
        for i in pg.get("issues_sorted", []):
            L.append(f"  - [{i.get('code')} sev {i.get('severity')}] **{_md(i.get('title'))}** - evidence: {_md(i.get('evidence'))}. Fix: {_md(i.get('fix'))}")
        if rv.get("positives"):
            L.append(f"- **Positives:** {'; '.join(_md(x) for x in rv['positives'])}")
        if rv.get("would_abandon_here"):
            L.append(f"- **Would abandon here:** {_md(rv.get('abandon_reason'))}")
        L.append("")
    if a and not a.get("skipped"):
        L.append("## Generated output assessment")
        L.append(f"*Artifact:* {_md(a.get('artifact_type'))}")
        L.append("")
        if a.get("overall_reaction"):
            L.append(f"> {_md(a['overall_reaction'])}")
        L.append("")
        L.append("| Criterion | Score (1-5) | Evidence |")
        L.append("|---|---|---|")
        for r in c["criteria"]:
            L.append(f"| {r['name']} | {r['score']} | {_md(r['evidence'])[:220]} |")
        fid = a.get("input_fidelity") or {}
        if fid:
            L.append("")
            for k in ("used_correctly", "missing", "changed", "invented"):
                if fid.get(k):
                    L.append(f"- **{k.replace('_', ' ')}:** {'; '.join(map(_md, fid[k]))}")
        L.append("")
        L.append("### Part by part")
        for part in a.get("parts") or []:
            if not isinstance(part, dict):
                continue
            L.append(f"#### {_md(part.get('part'))}")
            for ref in part.get("image_refs") or []:
                im = c["images"].get(ref)
                if im:
                    L.append(f"![{ref}]({im['path']})")
            if part.get("text"):
                L.append(f"> {_md(part['text'])[:800]}")
            if part.get("picture_description"):
                L.append(f"- *Picture:* {_md(part['picture_description'])}")
            L.append(f"- *Reaction:* {_md(part.get('reaction'))}")
            for pr in part.get("problems") or []:
                if isinstance(pr, dict):
                    L.append(f"  - [{_md(pr.get('criterion'))}, sev {pr.get('severity')}] {_md(pr.get('evidence'))}")
            if part.get("suggested_change"):
                L.append(f"- **Change I'd make:** {_md(part['suggested_change'])}")
            if part.get("rewrite"):
                L.append(f"- **Suggested rewrite:** {_md(part['rewrite'])}")
            L.append("")
        if a.get("top_changes"):
            L.append("**Top changes to the output:** " + " | ".join(f"{i + 1}. {_md(x)}" for i, x in enumerate(a["top_changes"])))
            L.append("")
    if d.get("recommendations"):
        L.append("## Recommendations (participant's priorities)")
        for r in d["recommendations"]:
            if isinstance(r, dict):
                L.append(f"- **[{r.get('priority')}] {_md(r.get('change'))}** ({_md(r.get('page'))}) - {_md(r.get('why'))}")
        L.append("")
    L.append("## Interview")
    for q, ans in c["interview"]:
        if ans:
            L.append(f"- **{q}** {_md(ans)}")
    L.append("")
    L.append("## Session log")
    L.append("| Step | Screen | Emotion | Think-aloud | Actions |")
    L.append("|---|---|---|---|---|")
    for t in c["trace"]:
        o = t.get("output") or {}
        acts = "; ".join(f"{r['action'].get('type')}{'' if r['ok'] else ' (FAILED)'}" for r in t.get("results", []))
        L.append(f"| {t['step']} | {_md(t.get('title'))[:40]} | {_md(o.get('emotion'))} ({o.get('valence')}) | {_md(o.get('think_aloud'))[:220]} | {acts} |")
    return "\n".join(L) + "\n"
