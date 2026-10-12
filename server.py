"""Run the SAHE demo locally with camera permissions enabled on localhost."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print(f"SAHE demo running at http://{address[0]}:{address[1]}")
    print("Press Ctrl+C to stop.")
    ThreadingHTTPServer(address, SimpleHTTPRequestHandler).serve_forever()
