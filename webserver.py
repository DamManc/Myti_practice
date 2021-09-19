from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import cgi
from fase_2 import Student

students = []


class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return False
        message = json.loads(self.rfile.read(int(self.headers.get('content-length'))))
        students.clear()
        for student in message:
            new_student = Student(student['firstname'], student['lastname'], student['birthdate'], student['grades'])
            students.append(new_student.__dict__)
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes(json.dumps({'students': students}), 'utf-8'))


def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    run()
