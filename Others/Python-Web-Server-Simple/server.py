from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = 'localhost'
PORT = 8080

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            print('send Response = 200')
        except:
            file_to_open = "File not found"
            self.send_response(404)
            print('send Response = 404')

        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


httpd = HTTPServer(('localhost', PORT), Serv)
print(f'Server is Running\nHost = {HOST}\nPORT = {PORT}')
httpd.serve_forever()
