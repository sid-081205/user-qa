"""Build a static website for browsing finished runs.

For every session it shows the persona and the task it was given, each step with the exact prompt sent to the
model and the model's answer, what the persona typed, what the site produced, the part-by-part critique, the
questionnaire, the fidelity audit and, on StoryHearth, the ground-truth scores. A comparison page puts the
personas side by side. Nothing is re-run: the pages are built from the JSON records in each run directory.
"""
from __future__ import annotations

import html
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any, Iterable
from urllib.parse import quote, urlparse

import yaml

from ..evaluation.questionnaires import INTERVIEW, SUS_ITEMS, UEQS_ITEMS

ROOT = Path(__file__).resolve().parents[2]
GT_PATH = ROOT / "demo_sites" / "storyhearth" / "ground_truth.json"
SEV_LABEL = {0: "none", 1: "cosmetic", 2: "minor", 3: "major", 4: "catastrophic"}
NEW_PAGE = '<span class="badge">new page</span>'
FOUND = '<span class="badge b-good">found</span>'
MISSED = '<span class="badge b-grey">missed</span>'


def e(x: Any) -> str:
    return "" if x is None else html.escape(str(x))


def _json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def _jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text().splitlines():
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return out


def _num(x: Any) -> float | None:
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _fmt(x: Any, digits: int = 1) -> str:
    v = _num(x)
    return "–" if v is None else f"{v:.{digits}f}".rstrip("0").rstrip(".") if digits else f"{v:.0f}"


def _pct(x: Any) -> str:
    v = _num(x)
    return "–" if v is None else f"{100 * v:.0f}%"


def _avg(xs: Iterable[Any]) -> float | None:
    vals = [v for v in (_num(x) for x in xs) if v is not None]
    return mean(vals) if vals else None


class Run:
    def __init__(self, run_dir: Path, base: Path):
        self.dir = run_dir
        self.name = run_dir.name
        rel = run_dir.relative_to(base) if run_dir.is_relative_to(base) else Path(run_dir.name)
        self.group_dir = rel.parent.as_posix() if rel.parent != Path(".") else base.name
        self.slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", rel.as_posix())
        self.config = _json(run_dir / "config.json", {}) or {}
        self.summary = _json(run_dir / "summary.json", {}) or {}
        self.session = _json(run_dir / "session.json", {}) or {}
        self.assessment = _json(run_dir / "output_assessment.json", {}) or {}
        self.debrief = _json(run_dir / "debrief.json", {}) or {}
        self.fidelity = _json(run_dir / "fidelity.json", {}) or {}
        self.gt = _json(run_dir / "gt_scores.json")
        self.trace = _jsonl(run_dir / "trace.jsonl")
        self.calls = _jsonl(run_dir / "llm_calls.jsonl")
        try:
            self.persona = yaml.safe_load((run_dir / "persona.yaml").read_text()) or {}
        except FileNotFoundError:
            self.persona = {}
        self.extra_files = sorted(p.name for p in run_dir.glob("*.json")
                                  if p.name not in {"config.json", "summary.json", "session.json", "output_assessment.json",
                                                    "debrief.json", "fidelity.json", "gt_scores.json"})

    @property
    def site(self) -> str:
        return (self.config.get("site") or {}).get("name") or "site"

    @property
    def persona_id(self) -> str:
        return self.persona.get("id") or self.config.get("persona") or "persona"

    @property
    def persona_name(self) -> str:
        if self.persona_id == "generic_user":
            return "Generic user (no persona)"
        return self.persona.get("name") or self.persona_id

    @property
    def group(self) -> str:
        return self.group_dir or "runs"

    @property
    def status(self) -> str:
        if self.session.get("status"):
            return self.session["status"]
        return "incomplete" if self.trace else "no steps"


def discover(paths: list[Path]) -> list[Path]:
    found = set()
    for p in paths:
        if (p / "trace.jsonl").exists() or (p / "session.json").exists():
            found.add(p.resolve())
            continue
        for f in p.rglob("trace.jsonl"):
            if "_code" not in f.parts:
                found.add(f.parent.resolve())
    return sorted(found)


class Media:
    """Resolves run-relative picture paths for a page, optionally copying downscaled versions into the site."""

    def __init__(self, out: Path, copy: bool, max_px: int):
        self.out, self.copy, self.max_px = out, copy, max_px

    def src(self, run: Run, rel: str, page_dir: Path) -> str | None:
        if not rel:
            return None
        path = run.dir / rel
        if not path.exists():
            return None
        target = path
        if self.copy:
            target = self.out / "media" / run.slug / rel
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                try:
                    from PIL import Image

                    with Image.open(path) as im:
                        im.thumbnail((self.max_px, self.max_px * 3))
                        im.convert("RGB").save(target.with_suffix(".jpg") if target.suffix.lower() != ".jpg" else target, quality=72)
                    if target.suffix.lower() != ".jpg":
                        target = target.with_suffix(".jpg")
                except Exception:
                    target.write_bytes(path.read_bytes())
        return quote(Path(os.path.relpath(target.resolve(), page_dir.resolve())).as_posix())

    def img(self, run: Run, rel: str, page_dir: Path, alt: str = "", cls: str = "shot") -> str:
        src = self.src(run, rel, page_dir)
        if not src:
            label = alt or Path(rel or "").name
            return f'<div class="noimg">Picture not in this copy{": " + e(label[:160]) if label else ""}</div>'
        return f'<a href="{src}" target="_blank"><img class="{cls}" loading="lazy" src="{src}" alt="{e(alt)}" title="{e(alt)}"></a>'


CSS = """
:root{--bg:#f6f7fb;--card:#fff;--ink:#1f2330;--muted:#6b7280;--line:#e5e7eb;--accent:#4f46e5;--good:#047857;--bad:#b91c1c;--warn:#b45309}
*{box-sizing:border-box}body{margin:0;font:15px/1.55 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;background:var(--bg);color:var(--ink)}
a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
header.top{background:#111827;color:#fff;padding:14px 28px;display:flex;gap:24px;align-items:center;flex-wrap:wrap}
header.top a{color:#c7d2fe}header.top .brand{font-weight:700;color:#fff;font-size:17px}
nav.sec{position:sticky;top:0;z-index:5;background:rgba(246,247,251,.95);backdrop-filter:blur(6px);border-bottom:1px solid var(--line);padding:8px 28px;display:flex;gap:18px;flex-wrap:wrap;font-size:14px}
main{max-width:1240px;margin:0 auto;padding:22px 28px 80px}
h1{font-size:26px;margin:6px 0 4px}h2{font-size:21px;margin:34px 0 12px;padding-top:8px}h3{font-size:16px;margin:18px 0 8px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:12px 0;box-shadow:0 1px 2px rgba(0,0,0,.03)}
.muted{color:var(--muted)}.small{font-size:13px}.grid{display:grid;gap:14px}.g2{grid-template-columns:repeat(auto-fit,minmax(320px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
.kpis{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0}.kpi{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:8px 14px;min-width:110px}
.kpi b{display:block;font-size:20px}.kpi span{font-size:12px;color:var(--muted)}
table{border-collapse:collapse;width:100%;background:var(--card);font-size:14px}th,td{border-bottom:1px solid var(--line);padding:7px 9px;text-align:left;vertical-align:top}
th{background:#f3f4f6;font-weight:600;font-size:13px;position:sticky;top:41px}.scroll{overflow-x:auto}.scroll th{position:static}
.badge{display:inline-block;border-radius:999px;padding:1px 9px;font-size:12px;font-weight:600;background:#eef2ff;color:#3730a3;margin-right:4px}
.b-good{background:#d1fae5;color:#065f46}.b-bad{background:#fee2e2;color:#991b1b}.b-warn{background:#fef3c7;color:#92400e}.b-grey{background:#f3f4f6;color:#374151}
.sev0,.sev1{background:#f3f4f6;color:#374151}.sev2{background:#fef3c7;color:#92400e}.sev3{background:#fed7aa;color:#9a3412}.sev4{background:#fee2e2;color:#991b1b}
blockquote{margin:8px 0;padding:8px 14px;border-left:4px solid #a5b4fc;background:#f5f7ff;border-radius:0 8px 8px 0;font-style:italic}
pre{white-space:pre-wrap;word-break:break-word;background:#0f172a;color:#e2e8f0;padding:12px 14px;border-radius:8px;font-size:12.5px;line-height:1.45;max-height:560px;overflow:auto}
pre.light{background:#f8fafc;color:var(--ink);border:1px solid var(--line)}
details{margin:8px 0}summary{cursor:pointer;font-weight:600;color:#374151}details[open]>summary{margin-bottom:6px}
.step{display:grid;grid-template-columns:minmax(260px,420px) 1fr;gap:16px}@media(max-width:900px){.step{grid-template-columns:1fr}}
img.shot{width:100%;border:1px solid var(--line);border-radius:8px;background:#fff}img.thumb{height:150px;border:1px solid var(--line);border-radius:6px;margin:0 6px 6px 0}
.gallery{display:flex;flex-wrap:wrap}.noimg{border:1px dashed #cbd5e1;border-radius:8px;padding:14px;color:var(--muted);font-size:13px;background:#fafafa;margin:0 6px 6px 0}
.role{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);margin-top:8px}
.imgtag{display:inline-block;background:#e0e7ff;color:#3730a3;border-radius:6px;padding:2px 8px;font-size:12px;margin:4px 0}
.part{border-left:4px solid #c7d2fe}.ok{color:var(--good)}.fail{color:var(--bad)}
ul.tight{margin:4px 0;padding-left:20px}ul.tight li{margin:2px 0}.cell-quote{font-size:13px;font-style:italic}
.bar{height:8px;background:#e5e7eb;border-radius:6px;overflow:hidden;width:110px;display:inline-block;vertical-align:middle;margin-right:6px}.bar i{display:block;height:100%;background:var(--accent)}
"""


def page(title: str, body: str, nav: str = "", depth: int = 0) -> str:
    up = "../" * depth
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{e(title)}</title><style>{CSS}</style></head><body>'
            f'<header class="top"><a class="brand" href="{up}index.html">userqa run explorer</a><a href="{up}index.html">All sessions</a>'
            f'<a href="{up}compare.html">Compare personas</a></header>{nav}<main>{body}</main></body></html>')


def valence_badge(v: Any) -> str:
    n = _num(v)
    if n is None:
        return ""
    cls = "b-good" if n > 0 else "b-bad" if n < 0 else "b-grey"
    return f'<span class="badge {cls}">valence {n:+.0f}</span>'


def sev_badge(s: Any) -> str:
    n = int(_num(s) or 0)
    return f'<span class="badge sev{n}">sev {n} · {SEV_LABEL.get(n, "")}</span>'


def ul(items: Iterable[Any]) -> str:
    items = [i for i in items if i not in (None, "")]
    if not items:
        return '<p class="muted small">none</p>'
    return '<ul class="tight">' + "".join(f"<li>{e(i if not isinstance(i, dict) else _dict_line(i))}</li>" for i in items) + "</ul>"


def _dict_line(d: dict) -> str:
    return "; ".join(f"{k}: {v}" for k, v in d.items() if v not in (None, "", [], {}))


def render_messages(req: list[dict], screenshot_html: str = "") -> str:
    out = []
    for m in req or []:
        out.append(f'<div class="role">{e(m.get("role"))}</div>')
        c = m.get("content")
        if isinstance(c, str):
            out.append(f"<pre>{e(c)}</pre>")
            continue
        for part in c or []:
            if part.get("type") == "text":
                out.append(f"<pre>{e(part.get('text'))}</pre>")
            elif part.get("type") == "image_url":
                out.append('<span class="imgtag">picture sent to the model</span>' + (screenshot_html if screenshot_html else ""))
                screenshot_html = ""
    return "".join(out)


def render_response(call: dict) -> str:
    raw = call.get("response")
    try:
        body = json.dumps(json.loads(raw), indent=2, ensure_ascii=False)
    except (TypeError, json.JSONDecodeError):
        body = raw if isinstance(raw, str) else json.dumps(raw, indent=2, ensure_ascii=False)
    out = f"<pre>{e(body)}</pre>"
    if call.get("reasoning"):
        out += f'<details><summary>Model reasoning ({len(call["reasoning"]):,} characters)</summary><pre class="light">{e(call["reasoning"])}</pre></details>'
    return out


def call_meta(call: dict) -> str:
    u = call.get("usage") or {}
    return (f'{e(call.get("purpose"))} · {e(call.get("served_model") or call.get("model"))} · {_fmt(call.get("seconds"))} s · '
            f'{u.get("prompt_tokens", "?"):,} prompt + {u.get("completion_tokens", "?"):,} completion tokens'
            if isinstance(u.get("prompt_tokens"), int) and isinstance(u.get("completion_tokens"), int)
            else f'{e(call.get("purpose"))} · {e(call.get("model"))}')


def call_block(call: dict, screenshot_html: str = "") -> str:
    return (f'<details><summary>Prompt sent to the model <span class="muted small">({call_meta(call)})</span></summary>'
            f'{render_messages(call.get("request") or [], screenshot_html)}</details>'
            f'<details><summary>What the model answered</summary>{render_response(call)}</details>')


class Explorer:
    def __init__(self, runs: list[Run], out: Path, media: Media):
        self.runs, self.out, self.media = runs, out, media
        gt = _json(GT_PATH, {}) or {}
        self.defects = {d["id"]: d for d in gt.get("defects", [])}

    def build(self) -> Path:
        (self.out / "runs").mkdir(parents=True, exist_ok=True)
        for r in self.runs:
            (self.out / "runs" / f"{r.slug}.html").write_text(self.run_page(r))
        (self.out / "index.html").write_text(self.index_page())
        (self.out / "compare.html").write_text(self.compare_page())
        return self.out / "index.html"

    # ---------- index

    def groups(self) -> dict[str, list[Run]]:
        g: dict[str, list[Run]] = defaultdict(list)
        for r in self.runs:
            g[r.group].append(r)
        labelled = {}
        for folder, runs in sorted(g.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            sites = ", ".join(dict.fromkeys(r.site for r in runs))
            labelled[f"{sites} · {folder}"] = runs
        return labelled

    def index_page(self) -> str:
        body = ['<h1>Simulated-user sessions</h1><p class="muted">Each session is one persona using one website. Open a session to see '
                "the task it was given, every step with the exact prompt sent to the model and its answer, everything the persona typed, "
                "everything the site produced, and the persona's critique of each part. "
                '<a href="compare.html">Compare personas</a> puts them side by side.</p>']
        for name, runs in self.groups().items():
            has_gt = any(r.gt for r in runs)
            body.append(f'<h2>{e(name)} <span class="muted small">({len(runs)} sessions)</span></h2>')
            head = ["Session", "Persona", "Status", "Steps", "Pages", "Issues", "Output parts", "Keepsake (1–5)", "SUS", "Mean valence", "LLM calls"]
            if has_gt:
                head[6:6] = ["UX recall", "Output recall"]
            rows = []
            for r in runs:
                s, j = r.summary, (r.gt or {}).get("judge") or {}
                cells = [f'<a href="runs/{r.slug}.html">{e(r.name)}</a><br><span class="muted small">{e(r.site)}</span>',
                         f'<b>{e(r.persona_name)}</b><br><span class="muted small">{e(r.persona.get("tagline", ""))}</span>',
                         e(r.status), e(s.get("steps", len(r.trace))), e(s.get("pages_reviewed", "–")), e(s.get("unique_issues", "–")),
                         e(s.get("output_parts", "–")), e(s.get("keepsake_worthiness", "–")), _fmt(s.get("sus")), _fmt(s.get("mean_valence"), 2),
                         e((s.get("llm_usage") or {}).get("calls", len(r.calls)))]
                if has_gt:
                    cells[6:6] = [_pct((j.get("ux") or {}).get("raw")), _pct((j.get("output") or {}).get("raw"))]
                rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
            body.append("<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join(rows) + "</table>")
        return page("userqa run explorer", "".join(body))

    # ---------- comparison

    def compare_page(self) -> str:
        body = ['<h1>Compare personas</h1><p class="muted">The same site seen by different kinds of user: their scores, what they '
                "thought of each page on first sight, how they judged what the site generated, and what they would change.</p>"]
        heat = ROOT / "paper" / "generated" / "figures" / "heatmap.png"
        for name, runs in self.groups().items():
            by_p: dict[str, list[Run]] = defaultdict(list)
            for r in runs:
                by_p[r.persona_id].append(r)
            body.append(f'<h2>{e(name)}</h2>')
            head = ["Persona", "Sessions", "SUS", "Keepsake (1–5)", "Mean valence", "Issues"]
            has_gt = any(r.gt for r in runs)
            if has_gt:
                head += ["UX recall", "Output recall", "Strict precision"]
            rows = []
            for pid, rs in by_p.items():
                cells = [f'<b>{e(rs[0].persona_name)}</b><br><span class="muted small">{e(rs[0].persona.get("tagline", ""))}</span>',
                         " ".join(f'<a href="runs/{r.slug}.html">{i + 1}</a>' for i, r in enumerate(rs)),
                         _fmt(_avg(r.summary.get("sus") for r in rs)), _fmt(_avg(r.summary.get("keepsake_worthiness") for r in rs)),
                         _fmt(_avg(r.summary.get("mean_valence") for r in rs), 2), _fmt(_avg(r.summary.get("unique_issues") for r in rs))]
                if has_gt:
                    js = [(r.gt or {}).get("judge") or {} for r in rs if r.gt]
                    cells += [_pct(_avg((j.get("ux") or {}).get("raw") for j in js)), _pct(_avg((j.get("output") or {}).get("raw") for j in js)),
                              _pct(_avg(j.get("precision_strict") for j in js))]
                rows.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
            body.append("<table><tr>" + "".join(f"<th>{h}</th>" for h in head) + "</tr>" + "".join(rows) + "</table>")
            if has_gt and heat.exists() and "storyhearth" in name.lower():
                (self.out / "assets").mkdir(exist_ok=True)
                (self.out / "assets" / "heatmap.png").write_bytes(heat.read_bytes())
                body.append('<div class="card"><h3>Which seeded defects each persona found</h3><img class="shot" src="assets/heatmap.png" '
                            'alt="Detection rate per seeded defect and persona"><p class="muted small">Share of each persona\'s sessions that '
                            "reported each seeded defect (U = usability, O = output), from the paper.</p></div>")

            body.append("<h3>How each persona judged what the site generated</h3>")
            cards = []
            for pid, rs in by_p.items():
                inner = []
                for i, r in enumerate(rs):
                    a = r.assessment
                    if not (a.get("overall_reaction") or r.debrief.get("one_line_verdict")):
                        continue
                    inner.append(f'<p class="small muted"><a href="runs/{r.slug}.html#critique">session {i + 1}</a> · keepsake '
                                 f'{e(a.get("keepsake_worthiness", "–"))}/5 · would pay: {e(str(a.get("would_pay_for_it", "–"))[:90])}</p>'
                                 f'<blockquote>{e(a.get("overall_reaction", ""))}</blockquote>'
                                 + (f'<p class="small"><b>Verdict:</b> {e(r.debrief.get("one_line_verdict"))}</p>' if r.debrief.get("one_line_verdict") else ""))
                changes = (rs[0].assessment.get("top_changes") or [])[:3]
                if changes:
                    inner.append("<p class=\"small\"><b>Top changes to the output</b></p>" + ul(changes))
                if inner:
                    cards.append(f'<div class="card"><h3>{e(rs[0].persona_name)}</h3>{"".join(inner)}</div>')
            body.append('<div class="grid g2">' + "".join(cards) + "</div>" if cards else '<p class="muted">No output was assessed.</p>')

            if len(by_p) > 1:
                pages: dict[str, dict[str, tuple[str, Run]]] = defaultdict(dict)
                order: dict[str, int] = {}
                for pid, rs in by_p.items():
                    for r in rs:
                        for p in (r.session.get("pages") or {}).values():
                            key = urlparse(p.get("url") or "").path or p.get("page_key", "")
                            order.setdefault(key, p.get("first_step", 99))
                            fi = (p.get("review") or {}).get("first_impression")
                            if fi and pid not in pages[key]:
                                pages[key][pid] = (fi, r)
                keys = sorted(pages, key=lambda k: order.get(k, 99))
                pids = list(by_p)
                body.append('<h3>First impression of each page</h3><div class="scroll"><table><tr><th>Page</th>'
                            + "".join(f"<th>{e(by_p[p][0].persona_name)}</th>" for p in pids) + "</tr>")
                for k in keys:
                    body.append(f"<tr><td><code>{e(k)}</code></td>" + "".join(
                        f'<td class="cell-quote">{e(pages[k][p][0])} <a class="small" href="runs/{pages[k][p][1].slug}.html#journey">→</a></td>'
                        if p in pages[k] else '<td class="muted small">not reached</td>' for p in pids) + "</tr>")
                body.append("</table></div>")
        return page("Compare personas", "".join(body))

    # ---------- one session

    def run_page(self, r: Run) -> str:
        pd = self.out / "runs"
        sections = [("overview", "Persona & task", self.sec_overview(r)), ("journey", "Step by step (prompts & answers)", self.sec_journey(r, pd)),
                    ("io", "Inputs & outputs", self.sec_io(r, pd)), ("critique", "Output critique", self.sec_critique(r, pd)),
                    ("issues", "Page issues", self.sec_issues(r)), ("debrief", "Questionnaire & audit", self.sec_debrief(r))]
        if r.gt:
            sections.append(("scores", "Ground-truth scores", self.sec_scores(r)))
        sections.append(("calls", "All LLM calls", self.sec_calls(r)))
        nav = '<nav class="sec">' + "".join(f'<a href="#{a}">{e(t)}</a>' for a, t, _ in sections) + "</nav>"
        head = (f'<p class="muted small">{e(r.group)}</p><h1>{e(r.persona_name)} on {e(r.site)}</h1>'
                f'<p class="muted">{e(r.name)} · {e(r.status)}' + (f' · <a href="{quote(os.path.relpath(r.dir / "report.html", pd))}">classic report</a>'
                                                                   if (r.dir / "report.html").exists() and not self.media.copy else "") + "</p>")
        body = head + "".join(f'<section id="{a}"><h2>{e(t)}</h2>{html_}</section>' for a, t, html_ in sections)
        return page(f"{r.persona_name} · {r.name}", body, nav, depth=1)

    def sec_overview(self, r: Run) -> str:
        p, s, site = r.persona, r.summary, r.config.get("site") or {}
        u = s.get("llm_usage") or {}
        kpis = [("steps", s.get("steps", len(r.trace))), ("pages reviewed", s.get("pages_reviewed", "–")), ("issues", s.get("unique_issues", "–")),
                ("output parts", s.get("output_parts", "–")), ("keepsake 1–5", s.get("keepsake_worthiness", "–")),
                ("SUS", f'{_fmt(s.get("sus"))} {s.get("sus_grade", "")}'.strip()), ("mean valence", _fmt(s.get("mean_valence"), 2)),
                ("LLM calls", u.get("calls", len(r.calls))), ("minutes", _fmt((_num(s.get("wall_seconds")) or 0) / 60))]
        out = ['<div class="kpis">' + "".join(f'<div class="kpi"><b>{e(v)}</b><span>{e(k)}</span></div>' for k, v in kpis) + "</div>"]
        facts = [("Age", p.get("age")), ("Occupation", p.get("occupation")), ("Household", p.get("household")), ("Locale", p.get("locale")),
                 ("Device / attention", f'{r.config.get("device", "")} / {r.config.get("attention", "")}'), ("Patience (steps)", p.get("patience_steps"))]
        persona_html = (f'<div class="card"><h3>{e(p.get("name", r.persona_id))} <span class="muted small">({e(r.persona_id)})</span></h3>'
                        f'<p><i>{e(p.get("tagline", ""))}</i></p><blockquote>{e(p.get("backstory", ""))}</blockquote>'
                        + "".join(f"<div class=\"small\"><b>{e(k)}:</b> {e(v)}</div>" for k, v in facts if v not in (None, "", " / "))
                        + "<h3>Goals</h3>" + ul(p.get("goals") or []) + "<h3>Frustrations</h3>" + ul(p.get("frustrations") or [])
                        + f'<details><summary>Full persona definition</summary><pre class="light">{e(yaml.safe_dump(p, sort_keys=False, allow_unicode=True))}</pre></details></div>')
        prev = r.config.get("previous_run")
        task_html = (f'<div class="card"><h3>The task it was given</h3><pre class="light">{e(site.get("goal", ""))}</pre>'
                     f'<div class="small"><b>Start URL:</b> <a href="{e(site.get("url", ""))}">{e(site.get("url", ""))}</a></div>'
                     + (f'<div class="small"><b>Spending rule:</b> {e(site.get("spend_rule"))}</div>' if site.get("spend_rule") else "")
                     + (f'<div class="small"><b>Returning visit after:</b> {e(Path(str(prev)).name)}</div>' if prev else "")
                     + f'<div class="small"><b>Model:</b> {e(r.config.get("model"))} (temperature {e(r.config.get("temperature"))}); budget '
                     f'{e(r.config.get("max_steps"))} steps, {e(r.config.get("max_llm_calls"))} calls</div>'
                     f'<details><summary>Full site configuration</summary><pre class="light">{e(json.dumps(site, indent=2, ensure_ascii=False))}</pre></details>')
        sm = r.session.get("site_model") or {}
        if sm:
            task_html += "<h3>What the persona worked out the site is</h3>" + "".join(
                f'<div class="small"><b>{e(k.replace("_", " "))}:</b> {e(", ".join(map(str, v)) if isinstance(v, list) else v)}</div>' for k, v in sm.items())
        if r.session.get("final_summary"):
            task_html += f'<h3>How it ended</h3><p>{e(r.session["final_summary"])}</p>'
        ab = r.session.get("abandonment")
        if ab:
            task_html += f'<p><span class="badge b-warn">would have given up</span> at step {e(ab.get("step"))}: {e(ab.get("reason"))}</p>'
        task_html += "</div>"
        return "".join(out) + f'<div class="grid g2">{persona_html}{task_html}</div>'

    def sec_journey(self, r: Run, pd: Path) -> str:
        step_calls = [c for c in r.calls if c.get("purpose") == "step"]
        out = []
        for i, t in enumerate(r.trace):
            o = t.get("output") or {}
            shot = self.media.img(r, t.get("screenshot") or "", pd, f"step {t.get('step')} screenshot")
            acts = []
            for res in t.get("results") or []:
                a = res.get("action") or {}
                desc = " ".join(str(a.get(k)) for k in ("type",) if a.get(k)) + (f' #{a["id"]}' if a.get("id") is not None else "")
                if a.get("text"):
                    desc += f' “{str(a["text"])[:200]}”'
                mark = '<span class="ok">✓</span>' if res.get("ok") else '<span class="fail">✗</span>'
                acts.append(f"<li>{mark} <code>{e(desc)}</code> <span class=\"muted small\">{e(res.get('message'))}</span></li>")
            rv = o.get("page_review") or {}
            review = ""
            if rv:
                wt = rv.get("walkthrough") or {}
                review = (f'<details open><summary>Page review: {e(rv.get("page_name", ""))}</summary>'
                          f'<div class="small"><b>What is happening:</b> {e(rv.get("what_is_happening"))}</div>'
                          f'<div class="small"><b>Purpose:</b> {e(rv.get("purpose"))}</div>'
                          f'<blockquote>{e(rv.get("first_impression"))}</blockquote>'
                          + ("".join(f'<div class="small"><b>{e(k.split("_", 1)[0].upper())}</b> {e(v)}</div>' for k, v in wt.items()) if isinstance(wt, dict) else "")
                          + self.issue_list(rv.get("issues") or [])
                          + (f'<div class="small"><b>Positives:</b></div>{ul(rv.get("positives") or [])}' if rv.get("positives") else "")
                          + (f'<p><span class="badge b-warn">would give up here</span> {e(rv.get("abandon_reason"))}</p>' if rv.get("would_abandon_here") else "")
                          + "</details>")
            new_issues = self.issue_list(o.get("new_issues") or [], "Issues noticed at this step") if o.get("new_issues") else ""
            events = ("<div class=\"small\"><b>What the browser reported:</b></div>" + ul(t.get("events"))) if t.get("events") else ""
            call = step_calls[i] if i < len(step_calls) else None
            prompt = call_block(call) if call else '<p class="muted small">No model call recorded for this step.</p>'
            out.append(
                f'<div class="card" id="step-{e(t.get("step"))}"><h3>Step {e(t.get("step"))} · {e(t.get("title"))} '
                f'{NEW_PAGE if t.get("new_page") else ""}</h3>'
                f'<div class="muted small">{e(t.get("url"))}</div>'
                f'<p><span class="badge b-grey">{e(o.get("emotion"))}</span>{valence_badge(o.get("valence"))}'
                f'<span class="badge b-grey">ease {e(o.get("ease"))}</span></p>'
                f'<div class="step"><div>{shot}</div><div>'
                f'<div class="small muted">Thinking aloud</div><blockquote>{e(o.get("think_aloud"))}</blockquote>'
                + (f'<div class="small"><b>Did the last action work?</b> {e(o.get("last_action_feedback"))}</div>' if o.get("last_action_feedback") else "")
                + (f'<div class="small"><b>Reaction to the output:</b> {e(o.get("output_reaction"))}</div>' if o.get("output_reaction") else "")
                + f'<div class="small"><b>Plan:</b> {e(o.get("plan"))}</div>'
                f'<div class="small"><b>Actions</b></div><ul class="tight">{"".join(acts) or "<li class=muted>none</li>"}</ul>{events}'
                f"</div></div>{review}{new_issues}{prompt}</div>")
        for c in step_calls[len(r.trace):]:
            out.append(f'<div class="card"><h3>Model call without a recorded step</h3><p class="muted small">The session ended before this answer was '
                       f"acted on.</p>{call_block(c)}</div>")
        return "".join(out) or '<p class="muted">No steps recorded.</p>'

    def issue_list(self, issues: list, title: str = "Issues") -> str:
        items = [i for i in issues if isinstance(i, dict)]
        if not items:
            return ""
        rows = "".join(f'<li>{sev_badge(i.get("severity"))}<span class="badge b-grey">{e(i.get("code"))}</span><b>{e(i.get("title"))}</b>'
                       f'<div class="small">Evidence: {e(i.get("evidence"))}</div>'
                       + (f'<div class="small muted">Why it matters to me: {e(i.get("why_it_matters_to_me") or i.get("why"))}</div>'
                          if (i.get("why_it_matters_to_me") or i.get("why")) else "")
                       + (f'<div class="small">Fix: {e(i.get("fix"))}</div>' if i.get("fix") else "") + "</li>" for i in items)
        return f'<div class="small"><b>{e(title)}</b></div><ul class="tight">{rows}</ul>'

    def sec_io(self, r: Run, pd: Path) -> str:
        inputs = r.assessment.get("inputs") or r.session.get("inputs") or []
        cols = [k for k in ("visit", "step", "page", "field", "action", "value") if any(k in i for i in inputs)]
        extra = sorted({k for i in inputs for k in i} - set(cols) - {"id"})
        cols += extra
        out = [f'<h3>Everything the persona typed or chose ({len(inputs)})</h3>']
        if inputs:
            out.append("<table><tr>" + "".join(f"<th>{e(c)}</th>" for c in cols) + "</tr>" + "".join(
                "<tr>" + "".join(f"<td>{e(Path(str(i.get(c))).name if c == 'visit' and i.get(c) else i.get(c, ''))}</td>" for c in cols) + "</tr>"
                for i in inputs) + "</table>")
        else:
            out.append('<p class="muted">No inputs recorded.</p>')
        caps = r.session.get("captures") or []
        out.append(f'<h3>Everything the site produced that was captured ({len(caps)})</h3><p class="muted small">Pages with generated content, '
                   "downloaded files and pictures, in the order they were captured. Later versions of the same page replace earlier ones in the critique.</p>")
        for n, c in enumerate(caps, 1):
            d = r.dir / (c.get("dir") or "")
            text = (d / "text.txt").read_text() if (d / "text.txt").exists() else ""
            pics = [(im.get("path"), im.get("alt", "")) for im in c.get("images") or []] + [(v, "page view") for v in c.get("views") or []]
            gallery = "".join(self.media.img(r, pth, pd, alt, "thumb") for pth, alt in pics[:24])
            out.append(f'<div class="card"><h3>{n}. {e(c.get("label"))}</h3><div class="muted small">{e(c.get("url"))}'
                       f'{" · " + e(c.get("source")) if c.get("source") else ""}</div>'
                       f'<div class="gallery">{gallery}</div>'
                       + (f'<details><summary>Captured text ({len(text):,} characters)</summary><pre class="light">{e(text)}</pre></details>' if text else "")
                       + "</div>")
        return "".join(out)

    def sec_critique(self, r: Run, pd: Path) -> str:
        a = r.assessment
        if not a.get("parts"):
            return f'<p class="muted">{e(a.get("reason") or "The output was not assessed in this session.")}</p>'
        images = {im.get("ref"): im for im in a.get("images") or []}
        out = [f'<div class="card"><h3>{e(a.get("artifact_type"))}</h3><blockquote>{e(a.get("overall_reaction"))}</blockquote>'
               f'<p><span class="badge">keepsake {e(a.get("keepsake_worthiness"))}/5</span> <b>Would pay:</b> {e(a.get("would_pay_for_it"))}</p>']
        crit = a.get("criteria") or {}
        if crit:
            out.append("<table><tr><th>Criterion</th><th>Score (1–5)</th><th>Why</th></tr>" + "".join(
                f'<tr><td>{e(k.replace("_", " "))}</td><td><span class="bar"><i style="width:{20 * (_num(v.get("score")) or 0):.0f}%"></i></span>'
                f'{e(v.get("score"))}</td><td class="small">{e(v.get("evidence") or v.get("why"))}</td></tr>'
                for k, v in crit.items() if isinstance(v, dict)) + "</table>")
        fid = a.get("input_fidelity") or {}
        if fid:
            out.append('<h3>Did the output keep what the persona asked for?</h3><div class="grid g3">' + "".join(
                f'<div><b>{e(k.replace("_", " "))}</b>{ul(v if isinstance(v, list) else [v])}</div>' for k, v in fid.items()) + "</div>")
        if a.get("top_changes"):
            out.append("<h3>Top changes to the output</h3>" + ul(a["top_changes"]))
        if a.get("safety_concerns"):
            out.append("<h3>Safety</h3>" + ul(a["safety_concerns"]))
        out.append("</div><h3>Part by part</h3>")
        for p in a["parts"]:
            pics = "".join(self.media.img(r, (images.get(ref) or {}).get("path", ""), pd, (images.get(ref) or {}).get("desc", ref), "thumb")
                           for ref in p.get("image_refs") or [])
            probs = "".join(f'<li>{sev_badge(x.get("severity"))}<b>{e(x.get("criterion"))}</b> {e(x.get("evidence"))}</li>'
                            for x in p.get("problems") or [] if isinstance(x, dict))
            out.append(f'<div class="card part"><h3>{e(p.get("part"))}</h3>'
                       + (f'<div class="muted small">{e(p.get("artifact"))}</div>' if p.get("artifact") else "")
                       + f'<div class="step"><div><div class="gallery">{pics}</div>'
                       + (f'<pre class="light">{e(p.get("text"))}</pre>' if p.get("text") else "")
                       + (f'<div class="small"><b>Picture, as the critic saw it:</b> {e(p.get("picture_description"))}</div>' if p.get("picture_description") else "")
                       + f'</div><div><div class="small muted">Reaction</div><blockquote>{e(p.get("reaction"))}</blockquote>'
                       + (f'<div class="small"><b>Problems</b></div><ul class="tight">{probs}</ul>' if probs else "")
                       + (f'<div class="small"><b>Strengths</b></div>{ul(p.get("strengths"))}' if p.get("strengths") else "")
                       + (f'<div class="small"><b>Change I would make:</b> {e(p.get("suggested_change"))}</div>' if p.get("suggested_change") else "")
                       + (f'<div class="small"><b>Suggested rewrite:</b></div><pre class="light">{e(p.get("rewrite"))}</pre>' if p.get("rewrite") else "")
                       + "</div></div></div>")
        if a.get("version_changes"):
            out.append("<details><summary>What changed between versions of the same output</summary>" + ul(
                f'{v.get("part")}: {v.get("changes")}' for v in a["version_changes"]) + "</details>")
        if a.get("measurements"):
            out.append(f'<details><summary>Deterministic text measurements</summary><pre class="light">{e(json.dumps(a["measurements"], indent=2, ensure_ascii=False))}</pre></details>')
        if r.extra_files:
            out.append(f'<p class="muted small">Other records in this folder (earlier versions, ablations, re-runs): {e(", ".join(r.extra_files))}</p>')
        return "".join(out)

    def sec_issues(self, r: Run) -> str:
        pages = sorted((r.session.get("pages") or {}).values(), key=lambda p: p.get("first_step", 0))
        if not pages:
            return '<p class="muted">No page reviews recorded.</p>'
        out = []
        for p in pages:
            rv = p.get("review") or {}
            issues = [i for i in (rv.get("issues") or []) if isinstance(i, dict)] + [i for i in (p.get("later_issues") or []) if isinstance(i, dict)]
            issues.sort(key=lambda i: -(_num(i.get("severity")) or 0))
            out.append(f'<div class="card"><h3>{e(rv.get("page_name") or p.get("title"))} <span class="muted small">step {e(p.get("first_step"))}</span></h3>'
                       f'<div class="muted small">{e(p.get("url"))}</div>{self.issue_list(issues) or "<p class=muted>No issues.</p>"}</div>')
        return "".join(out)

    def sec_debrief(self, r: Run) -> str:
        d, f = r.debrief, r.fidelity
        if not d and not f:
            return '<p class="muted">No questionnaire or audit in this session.</p>'
        out = []
        if d:
            sus = d.get("sus_score") or {}
            out.append(f'<div class="card"><h3>Verdict</h3><blockquote>{e(d.get("one_line_verdict"))}</blockquote>'
                       f'<p><span class="badge">SUS {e(sus.get("score"))} ({e(sus.get("grade"))})</span>'
                       f'<span class="badge">likelihood to recommend {e(d.get("nps"))}/10</span>'
                       + "".join(f'<span class="badge b-grey">UEQ-S {e(k)} {_fmt(v, 2)}</span>' for k, v in (d.get("ueq_s_score") or {}).items()) + "</p>")
            items = []
            for x in d.get("sus") or []:
                try:
                    items.append(f'<tr><td>{e(SUS_ITEMS[int(x.get("item")) - 1])}</td><td>{e(x.get("rating"))}</td><td class="small">{e(x.get("reason"))}</td></tr>')
                except (TypeError, ValueError, IndexError):
                    continue
            if items:
                out.append("<details><summary>SUS answers</summary><table><tr><th>Statement</th><th>1–5</th><th>Reason</th></tr>" + "".join(items) + "</table></details>")
            ueq = [f"<tr><td>{e(a)} – {e(b)}</td><td>{e(x.get('rating') if isinstance(x, dict) else x)}</td></tr>"
                   for (a, b, _), x in zip(UEQS_ITEMS, d.get("ueq_s") or [])]
            if ueq:
                out.append("<details><summary>UEQ-S answers</summary><table><tr><th>Pair</th><th>Rating</th></tr>" + "".join(ueq) + "</table></details>")
            iv = d.get("interview") or {}
            out.append("<h3>Interview</h3>" + "".join(f'<div class="small"><b>{e(q)}</b></div><p>{e(iv.get(k))}</p>' for k, q in INTERVIEW if iv.get(k)))
            recs = [x for x in d.get("recommendations") or [] if isinstance(x, dict)]
            if recs:
                out.append("<h3>Recommendations</h3><table><tr><th>Priority</th><th>Change</th><th>Where</th><th>Why</th></tr>" + "".join(
                    f'<tr><td>{e(x.get("priority"))}</td><td>{e(x.get("change"))}</td><td class="small">{e(x.get("page"))}</td><td class="small">{e(x.get("why"))}</td></tr>'
                    for x in recs) + "</table>")
            out.append("</div>")
        if f:
            out.append('<div class="card"><h3>Persona-fidelity audit</h3><p class="muted small">A separate model call reads the whole transcript and '
                       "judges how faithfully the persona was played (1–5; lower is better for caricature and knowledge leakage).</p><table>"
                       + "".join(f'<tr><td>{e(k.replace("_", " "))}</td><td>{e(v.get("score") if isinstance(v, dict) else "")}</td>'
                                 f'<td class="small">{e(v.get("why") if isinstance(v, dict) else v)}</td></tr>'
                                 for k, v in f.items() if isinstance(v, dict) and "score" in v) + "</table>"
                       + "".join(f'<details><summary>{e(k.replace("_", " "))}</summary><pre class="light">{e(json.dumps(v, indent=2, ensure_ascii=False))}</pre></details>'
                                 for k, v in f.items() if not (isinstance(v, dict) and "score" in v)) + "</div>")
        return "".join(out)

    def sec_scores(self, r: Run) -> str:
        g = r.gt or {}
        j = g.get("judge") or {}
        det = set((j.get("ux") or {}).get("detected") or []) | set((j.get("output") or {}).get("detected") or [])
        out = [f'<div class="kpis"><div class="kpi"><b>{_pct((j.get("ux") or {}).get("raw"))}</b><span>UX recall</span></div>'
               f'<div class="kpi"><b>{_pct((j.get("output") or {}).get("raw"))}</b><span>output recall</span></div>'
               f'<div class="kpi"><b>{_pct(j.get("precision_strict"))}</b><span>strict precision</span></div>'
               f'<div class="kpi"><b>{_pct(j.get("precision_lenient"))}</b><span>lenient precision</span></div>'
               f'<div class="kpi"><b>{e(g.get("n_findings"))}</b><span>findings</span></div></div>',
               '<p class="muted small">An LLM judge matched each finding to at most one seeded defect. The same model plays the persona, and no '
               "person checked these matches.</p>"]
        if self.defects:
            out.append("<table><tr><th>Seeded defect</th><th>Found?</th><th>First step</th></tr>" + "".join(
                f'<tr><td><b>{e(d)}</b> {e(v.get("title"))}<div class="small muted">{e(v.get("description"))}</div></td>'
                f'<td>{FOUND if d in det else MISSED}</td>'
                f'<td>{e((j.get("first_step") or {}).get(d, ""))}</td></tr>' for d, v in self.defects.items()) + "</table>")
        fs = g.get("findings") or []
        if fs:
            out.append(f"<details><summary>All {len(fs)} findings and how the judge classed them</summary><table><tr><th>ID</th><th>Where</th>"
                       "<th>Finding</th><th>Severity</th><th>Judge</th></tr>" + "".join(
                           f'<tr><td>{e(x.get("fid"))}</td><td class="small">{e(x.get("where"))}</td><td><b>{e(x.get("title"))}</b>'
                           f'<div class="small muted">{e(str(x.get("evidence", ""))[:300])}</div></td><td>{e(x.get("severity"))}</td>'
                           f'<td><span class="badge b-grey">{e(x.get("judge_class"))}</span> {e(x.get("judge_defect") or "")}</td></tr>'
                           for x in fs) + "</table></details>")
        return "".join(out)

    def sec_calls(self, r: Run) -> str:
        if not r.calls:
            return '<p class="muted">No LLM calls recorded.</p>'
        out = ['<p class="muted small">Every request sent to the model in this session, in order, with its answer. Step calls are also shown '
               "under their step.</p>"]
        step_i = 0
        for n, c in enumerate(r.calls, 1):
            if c.get("purpose") == "step":
                step_i += 1
                step = r.trace[step_i - 1].get("step") if step_i <= len(r.trace) else None
                link = f' · <a href="#step-{e(step)}">see step {e(step)}</a>' if step is not None else ""
                out.append(f'<div class="card"><b>{n}. step call</b> <span class="muted small">{call_meta(c)}{link}</span></div>')
            else:
                out.append(f'<div class="card"><b>{n}. {e(c.get("purpose"))}</b>{call_block(c)}</div>')
        return "".join(out)


def build_explorer(paths: list[Path], out: Path, copy_media: bool = False, max_px: int = 1000) -> Path:
    paths = [Path(p) for p in paths]
    run_dirs = discover(paths)
    base = Path(os.path.commonpath([str(p.resolve()) for p in paths])) if paths else Path.cwd()
    if base in run_dirs:
        base = base.parent
    runs = [Run(d, base) for d in run_dirs]
    out.mkdir(parents=True, exist_ok=True)
    return Explorer(runs, out, Media(out, copy_media, max_px)).build()
