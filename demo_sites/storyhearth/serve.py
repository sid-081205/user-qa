"""Serve the StoryHearth benchmark site (only the ``site/`` directory is exposed).

    python demo_sites/storyhearth/serve.py --port 8765
"""
from __future__ import annotations

import argparse
import functools
import http.server
from pathlib import Path

SITE = Path(__file__).parent / "site"


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--host", default="127.0.0.1")
    a = ap.parse_args()
    handler = functools.partial(NoCacheHandler, directory=str(SITE))
    with http.server.ThreadingHTTPServer((a.host, a.port), handler) as srv:
        print(f"StoryHearth on http://{a.host}:{a.port}/")
        srv.serve_forever()


if __name__ == "__main__":
    main()
