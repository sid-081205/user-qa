"""Command-line interface.

Examples
--------
  python -m userqa run --site storyhearth --persona grandparent_storykeeper
  python -m userqa run --url https://example.com --persona-type "a techy teenager who games a lot"
  python -m userqa personas list
  python -m userqa report runs/<run-dir>
  python -m userqa quota
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .llm import DEFAULT_FALLBACKS, DEFAULT_MODEL, LLMClient
from .personas.generator import generate_persona, persona_yaml
from .personas.schema import list_personas, load_persona
from .runner import ROOT, load_env_file, load_site, run_session

DEFAULT_GOAL = (
    "You have just landed on this website. Work out what it is and whether it is for you, then try its main "
    "feature the way you naturally would. If it creates or generates something, look carefully at everything it "
    "produces. Do not pay real money."
)


def main(argv=None) -> int:
    load_env_file()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(line_buffering=True)
    ap = argparse.ArgumentParser(prog="userqa", description="Persona-grounded agentic UX and output evaluation")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("run", help="run one simulated-user session")
    r.add_argument("--site", help="site config name (experiments/sites/<name>.yaml) or path")
    r.add_argument("--url", help="ad-hoc target URL (instead of --site)")
    r.add_argument("--goal", help="task given to the persona (defaults to open exploration)")
    g = r.add_mutually_exclusive_group()
    g.add_argument("--persona", help="persona id from the library or a YAML path")
    g.add_argument("--persona-type", help='free-text user type to synthesise, e.g. "a techy dad" or "a family-oriented grandparent"')
    r.add_argument("--model", default=DEFAULT_MODEL)
    r.add_argument("--fallbacks", default=",".join(DEFAULT_FALLBACKS), help="comma-separated fallback models")
    r.add_argument("--max-steps", type=int)
    r.add_argument("--max-calls", type=int)
    r.add_argument("--temperature", type=float, default=0.7)
    r.add_argument("--headless", action="store_true", help="headless browser (CAPTCHAs are more likely)")
    r.add_argument("--no-vision", action="store_true", help="do not send screenshots to the model")
    r.add_argument("--abandon-mode", choices=["note", "stop"], default="note")
    r.add_argument("--no-fidelity", action="store_true", help="skip the persona-fidelity audit call")
    r.add_argument("--previous-run", help="run dir of this persona's earlier session on the site (a returning visit)")
    r.add_argument("--out", default=str(ROOT / "runs"))

    p = sub.add_parser("personas", help="list / show / generate personas")
    p.add_argument("action", choices=["list", "show", "generate"])
    p.add_argument("arg", nargs="?")
    p.add_argument("--site-hint", default="a consumer website")
    p.add_argument("-o", "--output")
    p.add_argument("--model", default=DEFAULT_MODEL)

    rep = sub.add_parser("report", help="re-render a run's report")
    rep.add_argument("run_dir")

    ra = sub.add_parser("reassess", help="re-run a finished run's output assessment without browsing again")
    ra.add_argument("run_dirs", nargs="+")
    ra.add_argument("--with-debrief", action="store_true", help="also re-run the SUS/UEQ-S debrief")
    ra.add_argument("--no-vision", action="store_true", help="assess without looking at pictures (alt text only)")
    ra.add_argument("--variant", default="", help="write output_assessment.<variant>.json and leave the run otherwise untouched")

    au = sub.add_parser("reaudit", help="re-run a finished run's persona-fidelity audit from its trace")
    au.add_argument("run_dirs", nargs="+")

    ex = sub.add_parser("explore", help="build a static website for browsing finished runs (prompts, inputs, outputs, critiques)")
    ex.add_argument("paths", nargs="*", default=[str(ROOT / "runs")], help="run directories or folders containing them (default: runs/)")
    ex.add_argument("--out", default=str(ROOT / "explorer"))
    ex.add_argument("--copy-media", action="store_true", help="copy downscaled screenshots and pictures into the site so it can be shared")
    ex.add_argument("--max-px", type=int, default=1000, help="longest side of copied pictures")

    sub.add_parser("quota", help="show OpenRouter key limits / free-model quota")

    a = ap.parse_args(argv)
    if a.cmd == "run":
        if a.site:
            site = load_site(a.site)
            if a.goal:
                site["goal"] = a.goal
        elif a.url:
            from urllib.parse import urlparse

            host = urlparse(a.url).hostname or ""
            site = {"name": host, "url": a.url, "goal": a.goal or DEFAULT_GOAL, "allowed_domains": [host.removeprefix("www.")]}
        else:
            ap.error("give --site or --url")
        if a.persona_type:
            llm = LLMClient(model=a.model, max_calls=3)
            persona = generate_persona(llm, a.persona_type, site_hint=site.get("site_hint", site["url"]))
            print(f"[persona] synthesised {persona.id}: {persona.short()}")
        else:
            persona = load_persona(a.persona or "generic_user")
        run_dir = run_session(
            site, persona, Path(a.out), model=a.model, fallbacks=[m for m in a.fallbacks.split(",") if m],
            max_steps=a.max_steps, max_llm_calls=a.max_calls, headless=a.headless, vision=not a.no_vision,
            abandon_mode=a.abandon_mode, temperature=a.temperature, skip_fidelity=a.no_fidelity,
            previous_run=Path(a.previous_run) if a.previous_run else None,
        )
        print(run_dir)
        return 0
    if a.cmd == "personas":
        if a.action == "list":
            for pid in list_personas():
                pp = load_persona(pid)
                print(f"{pid:<28} {pp.short()}")
        elif a.action == "show":
            print(persona_yaml(load_persona(a.arg)))
        else:
            llm = LLMClient(model=a.model, max_calls=3)
            pp = generate_persona(llm, a.arg, site_hint=a.site_hint)
            text = persona_yaml(pp)
            if a.output:
                Path(a.output).write_text(text)
            print(text)
        return 0
    if a.cmd == "explore":
        from .report.explorer import build_explorer

        print(build_explorer([Path(p) for p in a.paths], Path(a.out), copy_media=a.copy_media, max_px=a.max_px))
        return 0
    if a.cmd == "report":
        from .report.render import render_report

        render_report(Path(a.run_dir))
        print(Path(a.run_dir) / "report.html")
        return 0
    if a.cmd in ("reassess", "reaudit"):
        from .runner import reassess_run, reaudit_run

        for d in a.run_dirs:
            try:
                if a.cmd == "reaudit":
                    reaudit_run(Path(d))
                else:
                    reassess_run(Path(d), with_debrief=a.with_debrief, vision=False if a.no_vision else None, variant=a.variant)
            except Exception as e:  # one broken run must not stop a batch
                print(f"[{a.cmd}] {d}: ERROR {type(e).__name__}: {e}")
        return 0
    if a.cmd == "quota":
        q = LLMClient(max_calls=0).quota()
        print(json.dumps({k: q.get(k) for k in ("label", "is_free_tier", "usage", "limit", "free_model_daily_requests")}, indent=2))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
