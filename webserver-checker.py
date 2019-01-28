import socket
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 8000
PORT_CHECKED1 = 8082
PORT_CHECKED1 = 9092

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result1 = sock1.connect_ex(('127.0.0.1',PORT_CHECKED1))
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result2 = sock2.connect_ex(('127.0.0.1',PORT_CHECKED2))
        if result1 == 0 and result2 == 0:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Checker of Activemq')
        else:
            print("Health check failed")
        sock1.close()
        sock2.close()


httpd = HTTPServer(("", PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()
