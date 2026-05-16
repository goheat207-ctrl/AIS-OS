"""
Local HTTP server — receives morning brief JSON from n8n and writes it to disk.
Listens on localhost:5679. No dependencies beyond stdlib.
Start: python D:/AIS-OS/scripts/brief_writer_server.py
"""

import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

PORT = 5679
OUTPUT = Path("D:/AIS-OS/logs/morning-brief.json")

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/brief":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError as e:
            logging.error("Bad JSON: %s", e)
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"bad json")
            return

        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
        logging.info("Saved morning brief -> %s", OUTPUT)

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"ok": True, "path": str(OUTPUT)}).encode())

    def log_message(self, format, *args):
        pass  # suppress default per-request noise


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), Handler)
    logging.info("Brief writer listening on http://localhost:%d/brief", PORT)
    server.serve_forever()
