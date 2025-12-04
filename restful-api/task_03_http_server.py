#!/usr/bin/python3
"""
Simple HTTP Server implementing a basic RESTful-like API
using Python's http.server module.
"""

import http.server
import socketserver
import json

PORT = 8000


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom request handler for our simple API
    """

    def _set_headers(self, status_code=200, content_type="text/plain"):
        """Helper method to set common headers"""
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.send_header("Access-Control-Allow-Origin", "*")  # Optional: for testing
        self.end_headers()

    def do_GET(self):
        """Handle GET requests"""
        
        if self.path == "/" or self.path == "/index.html":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == "/status":
            self._set_headers(200, "text/plain")
            self.wfile.write(b"OK")

        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self._set_headers(200, "application/json")
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            # 404 for any undefined endpoint
            self._set_headers(404, "text/plain")
            self.wfile.write(b"Endpoint not found")


def run(server_class=socketserver.TCPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server"""
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Server running at http://localhost:{PORT}")
    print("Available endpoints:")
    print("  GET /          → Hello message")
    print("  GET /data      → JSON dataset")
    print("  GET /status    → OK")
    print("  GET /info      → API info")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
