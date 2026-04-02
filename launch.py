#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════╗
║      ONE PIECE — Local Server Launcher           ║
║      海賊王への道 — The Grand Adventure           ║
╚══════════════════════════════════════════════════╝

Run this file to launch the One Piece website locally.
Just double-click OR run: python3 launch.py
"""

import http.server
import socketserver
import webbrowser
import os
import threading
import time

PORT = 8080
FILE = "onepiece_ultimate.html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress logs for cleaner output

def open_browser():
    time.sleep(1.2)
    webbrowser.open(f"http://localhost:{PORT}/{FILE}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print("\n")
    print("  ☠  ══════════════════════════════════════  ☠")
    print("       ONE PIECE — 海賊王への道")
    print("       The Grand Adventure Encyclopedia")
    print("  ☠  ══════════════════════════════════════  ☠")
    print(f"\n  ► Server running at: http://localhost:{PORT}/{FILE}")
    print("  ► Opening your browser automatically...")
    print("  ► Press CTRL+C to stop the server\n")

    threading.Thread(target=open_browser, daemon=True).start()

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n  ⚓ Server stopped. Until next voyage, nakama! ⚓\n")
