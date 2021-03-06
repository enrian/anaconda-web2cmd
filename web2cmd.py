from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, json
import subprocess
import os

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        cmd=["python", os.environ['RUN_SCRIPT'].replace('"', '')]
        parsed_path = urlparse.urlparse(self.path)
        params = urlparse.parse_qs(parsed_path.query)
        for key, value in params.items():
            cmd.extend(["--"+key, value[0]])
        output=subprocess.check_output(cmd)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(output)
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('0.0.0.0', int(os.environ['PORT'])), GetHandler)
    print('Starting server at http://0.0.0.0:8080')
    server.serve_forever()
