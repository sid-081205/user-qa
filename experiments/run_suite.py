"""Run a persona x repetition grid of sessions against one site, in parallel subprocesses.

    python experiments/run_suite.py --site storyhearth --name main --reps 2 \
        --personas grandparent_storykeeper,tech_savvy_parent,busy_parent_mobile,esl_parent,low_vision_senior,privacy_conscious_parent,generic_user

Each session is a separate ``python -m userqa run`` process (own browser, own LLM budget), so one
failure never takes down the grid. ``manifest.json`` in the suite directory records every session
and is rewritten after each one finishes; ``--resume`` skips sessions that already succeeded.

Sessions run from a frozen copy of the package (``<suite>/_code``, taken when the suite is first
started or with ``--refresh-code``), so editing the code while a suite runs cannot change it; the
git revision and uncommitted diff at snapshot time are recorded in the manifest.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def ensure_storyhearth(url: str) -> subprocess.Popen | None:
    """Start the local benchmark server if the site under test is StoryHearth and it is not up."""
    u = urlparse(url)
    if u.hostname not in ("127.0.0.1", "localhost"):
        return None
    try:
        urllib.request.urlopen(url, timeout=3)
        return None
    except Exception:
        pass
    proc = subprocess.Popen(
        [sys.executable, str(ROOT / "demo_sites/storyhearth/serve.py"), "--port", str(u.port or 80)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    for _ in range(20):
        time.sleep(0.5)
        try:
            urllib.request.urlopen(url, timeout=3)
            return proc
        except Exception:
            continue
    proc.kill()
    raise RuntimeError(f"could not start the StoryHearth server at {url}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", required=True)
    ap.add_argument("--personas", required=True, help="comma-separated persona ids")
    ap.add_argument("--reps", type=int, default=1)
    ap.add_argument("--name", required=True, help="suite name (runs/suite/<name>)")
    ap.add_argument("--parallel", type=int, default=3)
    ap.add_argument("--model")
    ap.add_argument("--fallbacks", help="comma-separated fallback models ('' for none)")
    ap.add_argument("--no-vision", action="store_true")
    ap.add_argument("--max-steps", type=int)
    ap.add_argument("--max-calls", type=int)
    ap.add_argument("--temperature", type=float)
    ap.add_argument("--no-fidelity", action="store_true")
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--refresh-code", action="store_true", help="re-snapshot the package before running")
    ap.add_argument("--stagger", type=float, default=20.0, help="seconds between session launches")
    a = ap.parse_args()
    sys.stdout.reconfigure(line_buffering=True)

    from userqa.runner import load_site

    site = load_site(a.site)
    suite_dir = ROOT / "runs" / "suite" / a.name
    (suite_dir / "logs").mkdir(parents=True, exist_ok=True)
    manifest_path = suite_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {"sessions": []}
    manifest["suite"] = {k: v for k, v in vars(a).items() if k not in ("resume", "refresh_code")} | {"site_url": site["url"]}
    code_dir = suite_dir / "_code"
    if a.refresh_code or not (code_dir / "userqa").exists():
        shutil.rmtree(code_dir, ignore_errors=True)
        shutil.copytree(ROOT / "userqa", code_dir / "userqa", ignore=shutil.ignore_patterns("__pycache__"))
        git = lambda *args: subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout.strip()  # noqa: E731
        manifest.setdefault("code_snapshots", []).append(
            {"taken": time.strftime("%Y-%m-%dT%H:%M:%S"), "git_head": git("rev-parse", "HEAD"), "dirty": git("status", "--porcelain", "userqa"),
             "diff": git("diff", "HEAD", "--", "userqa")[:20000]}
        )
    done = {(s["persona"], s["rep"]) for s in manifest["sessions"] if s.get("returncode") == 0 and a.resume}
    manifest["sessions"] = [s for s in manifest["sessions"] if (s["persona"], s["rep"]) in done]
    lock = threading.Lock()

    def save() -> None:
        tmp = manifest_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(manifest, indent=2))
        tmp.replace(manifest_path)

    server = ensure_storyhearth(site["url"])
    personas = [p.strip() for p in a.personas.split(",") if p.strip()]
    jobs = [(p, r) for r in range(1, a.reps + 1) for p in personas if (p, r) not in done]
    print(f"[suite] {a.name}: {len(jobs)} sessions to run ({len(done)} already done), parallel={a.parallel}")

    def run(job: tuple[str, int], delay: float) -> None:
        persona, rep = job
        time.sleep(delay)
        cmd = [sys.executable, "-m", "userqa", "run", "--site", a.site, "--persona", persona, "--out", str(suite_dir)]
        for flag, val in (("--model", a.model), ("--max-steps", a.max_steps), ("--max-calls", a.max_calls), ("--temperature", a.temperature)):
            if val is not None:
                cmd += [flag, str(val)]
        if a.fallbacks is not None:
            cmd += ["--fallbacks", a.fallbacks]
        if a.no_vision:
            cmd.append("--no-vision")
        if a.no_fidelity:
            cmd.append("--no-fidelity")
        log = suite_dir / "logs" / f"{persona}_r{rep}.log"
        t0 = time.time()
        with log.open("w") as fh:
            rc = subprocess.call(cmd, cwd=code_dir, stdout=fh, stderr=subprocess.STDOUT,
                                 env={**os.environ, "PYTHONUNBUFFERED": "1", "USERQA_ROOT": str(ROOT)})
        lines = [ln.strip() for ln in log.read_text().splitlines() if ln.strip()]
        run_dir = next((ln for ln in reversed(lines) if Path(ln).is_dir() and str(suite_dir) in ln), None)
        rec = {"persona": persona, "rep": rep, "returncode": rc, "seconds": round(time.time() - t0, 1),
               "run_dir": str(Path(run_dir).relative_to(ROOT)) if run_dir else None, "log": str(log.relative_to(ROOT))}
        with lock:
            manifest["sessions"].append(rec)
            save()
        print(f"[suite] {persona} r{rep}: rc={rc} in {rec['seconds']:.0f}s -> {rec['run_dir']}")

    try:
        with ThreadPoolExecutor(max_workers=max(1, a.parallel)) as pool:
            for i, job in enumerate(jobs):
                pool.submit(run, job, a.stagger * min(i, a.parallel - 1) if i < a.parallel else 0.0)
    finally:
        save()
        if server:
            server.terminate()
    ok = sum(1 for s in manifest["sessions"] if s.get("returncode") == 0)
    print(f"[suite] finished: {ok}/{len(manifest['sessions'])} sessions succeeded; manifest {manifest_path.relative_to(ROOT)}")
    return 0 if ok == len(manifest["sessions"]) else 1


if __name__ == "__main__":
    sys.exit(main())
