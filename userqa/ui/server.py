"""Live session viewer.

``python -m userqa ui`` serves a page where you enter a website, optionally pick or describe a persona, and
start a session. The session runs as ``python -m userqa run`` in a subprocess (so a crash cannot take the
server down) with a headed browser; the page polls the run folder and shows each step as it lands: the
screenshot the persona saw, what it thought, how it felt, its review of the page, the issues it logged and
what it did next, then the critique of everything the site produced and the questionnaire. Finished runs
under ``runs/`` can be opened in the same view.
"""
from __future__ import annotations

import json
import mimetypes
import os
import re
import signal
import subprocess
import sys
import threading
import time
import uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote, urlparse

import yaml

from ..agent.loop import STOP_FILE
from ..personas.schema import list_personas, load_persona
from ..runner import ROOT

RUNS_ROOT = ROOT / "runs"
UI_RUNS = RUNS_ROOT / "ui"
SITES_DIR = ROOT / "experiments" / "sites"
STATIC = Path(__file__).parent / "static"
TRACE_DROP = ("a11y", "page_text", "events")
LOG_TAIL = 60

PHASES = [
    ("preparing", "Preparing the persona and browser"),
    ("browsing", "Browsing the site"),
    ("critiquing", "Critiquing what the site produced"),
    ("questionnaire", "Answering the questionnaire"),
    ("auditing", "Checking the persona stayed in character"),
    ("done", "Finished"),
]


def _json(path: Path, default: Any = None) -> Any:
    try:
        return json.loads(path.read_text())
    except (OSError, ValueError):
        return default


def read_trace(path: Path, since: int = 0) -> list[dict]:
    """Trace records after the first ``since``, without the bulky page dumps; a half-written last line is skipped."""
    out = []
    try:
        lines = path.read_text().splitlines()
    except OSError:
        return out
    for line in lines[since:]:
        try:
            rec = json.loads(line)
        except ValueError:
            break
        out.append({k: v for k, v in rec.items() if k not in TRACE_DROP})
    return out


def site_profiles() -> list[dict]:
    out = []
    for f in sorted(SITES_DIR.glob("*.yaml")):
        try:
            s = yaml.safe_load(f.read_text()) or {}
        except yaml.YAMLError:
            continue
        out.append({
            "id": f.stem, "name": s.get("name", f.stem), "url": s.get("url", ""),
            "goal": str(s.get("goal", "")).strip(), "max_steps": s.get("max_steps"),
            "signs_in": bool(s.get("inbox") or s.get("credentials")),
        })
    return out


def match_profile(url: str, profiles: list[dict] | None = None) -> str | None:
    """The site profile for a URL: same host, preferring the profile named after the host, then an exact URL match."""
    host = (urlparse(url).hostname or "").removeprefix("www.")
    if not host:
        return None
    same = [p for p in (profiles if profiles is not None else site_profiles())
            if (urlparse(p["url"]).hostname or "").removeprefix("www.") == host]
    if not same:
        return None
    label = host.split(".")[0]
    for p in same:
        if p["name"] == label or p["id"] == label:
            return p["id"]
    for p in same:
        if p["url"].rstrip("/") == url.rstrip("/"):
            return p["id"]
    return same[0]["id"]


def build_command(req: dict, out_dir: Path) -> list[str]:
    url = str(req.get("url") or "").strip()
    profile = str(req.get("profile") or "").strip()
    if not url and not profile:
        raise ValueError("Enter a website address.")
    if url and not re.match(r"^https?://", url):
        url = "https://" + url
    cmd = [sys.executable, "-m", "userqa", "run"]
    if profile:
        if not (SITES_DIR / f"{profile}.yaml").exists():
            raise ValueError(f"Unknown site profile {profile!r}.")
        cmd += ["--site", profile]
    if url:
        cmd += ["--url", url]
    persona_type = str(req.get("persona_type") or "").strip()
    persona = str(req.get("persona") or "").strip()
    if persona_type:
        cmd += ["--persona-type", persona_type]
    elif persona:
        if persona not in list_personas():
            raise ValueError(f"Unknown persona {persona!r}.")
        cmd += ["--persona", persona]
    goal = str(req.get("goal") or "").strip()
    if goal:
        cmd += ["--goal", goal]
    if req.get("max_steps"):
        cmd += ["--max-steps", str(max(1, min(80, int(req["max_steps"]))))]
    if req.get("headless"):
        cmd.append("--headless")
    cmd += ["--out", str(out_dir)]
    return cmd


class Job:
    def __init__(self, req: dict):
        self.id = time.strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex[:4]
        self.out = UI_RUNS / self.id
        self.out.mkdir(parents=True, exist_ok=True)
        self.cmd = build_command(req, self.out)
        self.log_path = self.out / "console.log"
        (self.out / "request.json").write_text(json.dumps(req, indent=2, ensure_ascii=False))
        env = os.environ | {"PYTHONUNBUFFERED": "1"}
        self._log = self.log_path.open("w")
        self.proc = subprocess.Popen(self.cmd, cwd=ROOT, stdout=self._log, stderr=subprocess.STDOUT, env=env,
                                     start_new_session=True)
        self.started = time.time()
        self.stop_requested = False

    @property
    def run_dir(self) -> Path | None:
        dirs = [d for d in self.out.iterdir() if d.is_dir()]
        return max(dirs, key=lambda d: d.stat().st_mtime) if dirs else None

    @property
    def running(self) -> bool:
        return self.proc.poll() is None

    def stop(self, force: bool = False) -> None:
        self.stop_requested = True
        rd = self.run_dir
        if rd is not None and not force:
            (rd / STOP_FILE).write_text("stop\n")
        elif self.running:
            os.killpg(self.proc.pid, signal.SIGINT if not force else signal.SIGTERM)


def log_tail(path: Path, n: int = LOG_TAIL) -> list[str]:
    try:
        lines = path.read_text(errors="replace").splitlines()
    except OSError:
        return []
    return [re.sub(r"sk-or-v1-[A-Za-z0-9]+", "[REDACTED]", ln) for ln in lines[-n:]]


def phase_of(run_dir: Path | None) -> str:
    if run_dir is None or not (run_dir / "config.json").exists():
        return "preparing"
    if (run_dir / "summary.json").exists():
        return "done"
    if (run_dir / "debrief.json").exists():
        return "auditing"
    if (run_dir / "output_assessment.json").exists():
        return "questionnaire"
    if (run_dir / "session.json").exists():
        return "critiquing"
    return "browsing"


def persona_card(run_dir: Path) -> dict:
    p = yaml.safe_load((run_dir / "persona.yaml").read_text()) if (run_dir / "persona.yaml").exists() else {}
    p = p or {}
    return {k: p.get(k) for k in ("id", "name", "age", "tagline", "occupation", "backstory", "goals", "frustrations", "device")}


def run_state(run_dir: Path | None, since: int = 0) -> dict:
    phase = phase_of(run_dir)
    st: dict[str, Any] = {"phase": phase, "phases": PHASES, "steps": [], "since": since}
    if run_dir is None:
        return st
    st["run"] = str(run_dir.relative_to(RUNS_ROOT)) if run_dir.is_relative_to(RUNS_ROOT) else str(run_dir)
    st["config"] = _json(run_dir / "config.json", {})
    st["persona"] = persona_card(run_dir)
    st["steps"] = read_trace(run_dir / "trace.jsonl", since)
    st["live"] = _json(run_dir / "live.json")
    s = _json(run_dir / "session.json")
    if s:
        st["session"] = {k: s.get(k) for k in ("status", "steps", "final_summary", "abandonment", "duration_s", "output_reactions", "inputs")}
        st["session"]["captures"] = len(s.get("captures") or [])
    a = _json(run_dir / "output_assessment.json")
    if a:
        st["assessment"] = {k: a.get(k) for k in ("skipped", "reason", "overall_reaction", "keepsake_worthiness", "would_pay_for_it",
                                                  "top_changes", "criteria", "parts", "images", "safety_concerns")}
    d = _json(run_dir / "debrief.json")
    if d:
        st["debrief"] = {k: d.get(k) for k in ("one_line_verdict", "interview", "recommendations", "sus_score", "ueq_s_score", "nps", "error")}
    f = _json(run_dir / "fidelity.json")
    if f:
        st["fidelity"] = f
    sm = _json(run_dir / "summary.json")
    if sm:
        st["summary"] = {k: sm.get(k) for k in ("status", "steps", "pages_reviewed", "unique_issues", "reached_output", "output_parts",
                                                "keepsake_worthiness", "sus", "sus_grade", "nps", "mean_valence", "wall_seconds", "llm_usage")}
    st["report"] = (run_dir / "report.html").exists()
    return st


def past_runs() -> list[dict]:
    out = []
    for cfg in RUNS_ROOT.rglob("config.json"):
        d = cfg.parent
        c = _json(cfg, {})
        sm = _json(d / "summary.json", {})
        site = c.get("site") or {}
        out.append({
            "run": str(d.relative_to(RUNS_ROOT)), "folder": str(d.parent.relative_to(RUNS_ROOT)),
            "site": site.get("name"), "url": site.get("url"), "persona": c.get("persona"),
            "started": c.get("started_utc"), "status": sm.get("status") or phase_of(d),
            "steps": sm.get("steps"), "live_site": not str(site.get("url", "")).startswith("http://127.0.0.1"),
            "mtime": cfg.stat().st_mtime,
        })
    out.sort(key=lambda r: (r["started"] or "", r["mtime"]), reverse=True)
    return out


def resolve_run(rel: str) -> Path | None:
    d = (RUNS_ROOT / rel).resolve()
    if not d.is_relative_to(RUNS_ROOT.resolve()) or not (d / "config.json").exists():
        return None
    return d


def resolve_media(run_dir: Path, rel: str) -> Path | None:
    """A picture inside the run folder, else its committed downscaled copy; never anything else."""
    from ..report.explorer import IMAGE_SUFFIXES, MEDIA_ROOT, media_copy_path

    p = (run_dir / rel).resolve()
    if p.suffix.lower() not in IMAGE_SUFFIXES:
        return None
    if p.is_relative_to(run_dir.resolve()) and p.is_file():
        return p
    c = media_copy_path(run_dir, rel)
    if c is not None and c.resolve().is_relative_to(MEDIA_ROOT.resolve()) and c.is_file():
        return c.resolve()
    return None


class App:
    def __init__(self):
        self.jobs: dict[str, Job] = {}
        self.lock = threading.Lock()

    def meta(self) -> dict:
        personas = [{"id": pid, "label": load_persona(pid).short()} for pid in list_personas()]
        return {
            "personas": personas, "profiles": site_profiles(),
            "key_present": bool(os.environ.get("OPENROUTER_API_KEY")),
            "display": bool(os.environ.get("DISPLAY")) or sys.platform in ("darwin", "win32"),
            "jobs": [self.job_info(j) for j in self.jobs.values()],
        }

    def start(self, req: dict) -> dict:
        with self.lock:
            if any(j.running for j in self.jobs.values()):
                raise ValueError("A session is already running. Stop it first.")
            if req.get("url") and not req.get("profile") and req.get("auto_profile", True):
                req["profile"] = match_profile(str(req["url"])) or ""
            job = Job(req)
            self.jobs[job.id] = job
        return self.job_info(job)

    def job_info(self, j: Job) -> dict:
        return {"job": j.id, "running": j.running, "returncode": j.proc.returncode, "stop_requested": j.stop_requested,
                "cmd": " ".join(a if " " not in a else repr(a) for a in j.cmd[1:]), "started": j.started}

    def job_state(self, job_id: str, since: int) -> dict:
        j = self.jobs.get(job_id)
        if j is None:
            raise KeyError(job_id)
        st = run_state(j.run_dir, since)
        st |= self.job_info(j)
        st["log"] = log_tail(j.log_path)
        if not j.running and st["phase"] != "done":
            st["phase"] = "stopped" if j.stop_requested else "failed"
        return st


def make_handler(app: App):
    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            pass

        def _send(self, body: bytes, ctype: str, status: int = 200, cache: bool = False) -> None:
            self.send_response(status)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "max-age=3600" if cache else "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _json(self, obj: Any, status: int = 200) -> None:
            self._send(json.dumps(obj, ensure_ascii=False).encode(), "application/json; charset=utf-8", status)

        def _error(self, msg: str, status: int = 400) -> None:
            self._json({"error": msg}, status)

        def do_GET(self):
            u = urlparse(self.path)
            q = {k: v[0] for k, v in parse_qs(u.query).items()}
            since = int(q.get("since", 0) or 0)
            if u.path in ("/", "/index.html"):
                return self._send((STATIC / "index.html").read_bytes(), "text/html; charset=utf-8")
            if u.path == "/api/meta":
                return self._json(app.meta())
            if u.path == "/api/runs":
                return self._json(past_runs())
            if u.path == "/api/state":
                if q.get("job"):
                    try:
                        return self._json(app.job_state(q["job"], since))
                    except KeyError:
                        return self._error("unknown session", 404)
                d = resolve_run(q.get("run", ""))
                if d is None:
                    return self._error("unknown run", 404)
                st = run_state(d, since)
                if st["phase"] != "done":
                    st["phase"] = "incomplete"
                return self._json(st)
            if u.path == "/media":
                d = resolve_run(q.get("run", ""))
                p = resolve_media(d, q.get("path", "")) if d else None
                if p is None:
                    return self._error("not found", 404)
                return self._send(p.read_bytes(), mimetypes.guess_type(p.name)[0] or "application/octet-stream", cache=True)
            if u.path == "/report":
                d = resolve_run(q.get("run", ""))
                if d is None or not (d / "report.html").exists():
                    return self._error("no report", 404)
                html = (d / "report.html").read_text()
                html = re.sub(r'(src|href)="(?!https?:|#|data:|/)([^"]+)"',
                              lambda m: f'{m.group(1)}="/media?run={quote(q["run"])}&path={quote(m.group(2))}"', html)
                return self._send(html.encode(), "text/html; charset=utf-8")
            self._error("not found", 404)

        def do_POST(self):
            u = urlparse(self.path)
            try:
                body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0) or 0)) or b"{}")
            except ValueError:
                return self._error("bad JSON")
            if u.path == "/api/start":
                try:
                    return self._json(app.start(body))
                except ValueError as e:
                    return self._error(str(e))
            if u.path == "/api/stop":
                j = app.jobs.get(str(body.get("job")))
                if j is None:
                    return self._error("unknown session", 404)
                j.stop(force=bool(body.get("force")))
                return self._json(app.job_info(j))
            self._error("not found", 404)

    return Handler


def serve(host: str = "127.0.0.1", port: int = 8787, open_browser: bool = False) -> None:
    app = App()
    httpd = ThreadingHTTPServer((host, port), make_handler(app))
    url = f"http://{host}:{port}/"
    print(f"[ui] open {url}  (Ctrl+C to quit)")
    if open_browser:
        import webbrowser

        threading.Timer(0.5, webbrowser.open, args=(url,)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        for j in app.jobs.values():
            if j.running:
                j.stop(force=True)
        httpd.server_close()
