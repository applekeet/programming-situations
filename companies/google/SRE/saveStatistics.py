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


"""

from time import time, sleep
import http.server
import socketserver

PORT = 8000

## Main Class which creates the solution.
class saveSatistics(object):
    """saveSatistics"""
    def __init__(self):
        super(saveSatistics, self).__init__()
        self.c = CircularLinkedList()
        for x in range(3000):
            self.c.insert(0)
        
        # keep the head on circular linked list moving each second
        starttime = time()
        print(starttime)
        while True:
            c.move_head()
            print("tick", time())
            sleep(1.0 - ((time() - starttime) % 1.0))


    def eventCalled(self):
        c.write_at_head(1)


    def start_server(self):
        Handler = http.server.SimpleHTTPRequestHandler


        with socketserver.ThreadingTCPServer(("", PORT), CustomHandler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()


class CustomHandler(Handler):
    def do_GET(self):
        if None != re.search('/event/*', self.path):
            num = float(self.path.split('/')[-1])
            print self.path.split('/')
            #This URL will trigger our sample function and send what it returns back to the browser
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(str(num*num)) #call sample function here
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
    ss = saveSatistics()
    ss.eventCalled()

        




