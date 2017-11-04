#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

DEFAULT_PORT=3000

class MYS(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>My name is onephone!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        length = self.headers.getheaders('content-length')
        data = self.rfile.read(int(length[0]))
        print('Received post data: %s' % data)
        ## body
        #result = cmdhandler.mainbody(data)
        result = data
        if result == {}:
            print('do_POST result is {}')
        else:
            self.wfile.write(result)
            print('do_POST result is {}')

def run(server_class=HTTPServer, handler_class=MYS, port=int(DEFAULT_PORT)):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv
    # curl -d "dir=left&step=3" http://localhost
    try:
        if len(argv) == 2:
            run(port=int(argv[1]))
        else:
            run()
    except Exception as e:
        print(e)
