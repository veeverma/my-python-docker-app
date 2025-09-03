from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

# Read the current date and time for the welcome message
# We'll use the server's location, which is Perth, Australia for this example
os.environ['TZ'] = 'Australia/Perth'
time.tzset()
current_time = time.strftime('%Y-%m-%d %H:%M:%S %Z')

# Define the web server's behaviour
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>My Python App</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<h1>Hello from your Kubernetes App!</h1>", "utf-8"))
        self.wfile.write(bytes(f"<p>This app is running in a Pod. The current server time in Perth is: {current_time}</p>", "utf-8"))
        # Display the Pod's name using an environment variable set by Kubernetes
        pod_name = os.environ.get('POD_NAME', 'Unknown')
        self.wfile.write(bytes(f"<p>Served by Pod: <b>{pod_name}</b></p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":
    webServer = HTTPServer(("0.0.0.0", 8000), MyServer)
    print("Server started on http://0.0.0.0:8000")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")