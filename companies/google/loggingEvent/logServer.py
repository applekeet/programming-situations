
"""

Task: save statistics for 1 hour of logs, with one second resolution.
it should be able to save statictics from everything on the server.

-- approach
Spin up a web server, which can take request from different
services on the server or outside and store logs for an event.

then as we require 1 hour logs max with 1 second resolution
we can use circular linked list to store 3600 points for each second.

we are only looking for count of event that happened in particular
time interval.




https://stackoverflow.com/questions/42009202/how-to-call-a-async-function-contained-in-a-class

"""

from time import time, sleep
import asyncio
from . import CLL_modified
import http.server
import socketserver

PORT = 8000

## Main Class which creates the solution.
class logServer(object):
    """logServer"""

    def __init__(self):
        self.c = CLL_modified.CircularLinkedList()
        for x in range(3000):
            self.c.insert(0)

    async def start_loop(self):
        self.c.write_at_head_per_second()

    async def start_server(self):
        with socketserver.ThreadingTCPServer(("", PORT), CustomHandler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()

    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            if None != re.search('/event/*', self.path):
                print(self.path.split('/'))
                #This URL will trigger our sample function and send what it returns back to the browser
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                self.wfile.write(str(383)) #call sample function here
                return
            if None != re.search('/second/*', self.path):
                num1 = float(self.path.split('/')[-1])
                num2 = float(self.path.split('/')[-2])
                #This URL will trigger our sample function and send what it returns back to the browser
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(str(num1*num2)) #call sample function here
                return
            if None != re.search('/minute/*', self.path):
                num1 = float(self.path.split('/')[-1])
                num2 = float(self.path.split('/')[-2])
                #This URL will trigger our sample function and send what it returns back to the browser
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(str(num1*num2)) #call sample function here
                return
            if None != re.search('/hour/*', self.path):
                #This URL will trigger our sample function and send what it returns back to the browser
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                self.wfile.write(str(num1*num2)) #call sample function here
                return
            else:   
                #serve files, and directory listings by following self.path from
                #current working directory
                SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    ss = logServer()
    print('passed')
    await ss.start_server()
    await ss.start_loop()

        




