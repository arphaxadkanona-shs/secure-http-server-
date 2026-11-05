from http.server import SimpleHTTPRequestHandler, HTTPServer

class SecureHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'")
        super().end_headers()


server = HTTPServer(("127.0.0.1", 8001), SecureHandler)

print("Secure test server running on http://127.0.0.1:8001")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.server_close()
