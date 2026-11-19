#!/usr/bin/env python3
"""RetroCast local test server.
Run:  python3 serve.py   then open http://localhost:8008"""
import http.server, socketserver, webbrowser, os, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8008
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map,
                      '.webmanifest': 'application/manifest+json', '.js': 'text/javascript'}
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    url = f'http://localhost:{PORT}'
    print(f'RetroCast is on the air at {url}  (Ctrl+C to sign off)')
    try: webbrowser.open(url)
    except Exception: pass
    httpd.serve_forever()
