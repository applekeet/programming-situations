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


class Node():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.nxt = None

class CircularLinkedList:
    """CircularLinkedList.

    init - to create a fixed size CircularLinkedList
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            new_node = Node(value)

            """ if there is exists a preivous node to head,
            we take that last_node, add new_node to next of last.
            and add last_node to the previous of new_node.
            """
            if self.head.prev is not None:
                # prev node exists
                last_node = self.head.prev
                last_node.nxt = new_node
                new_node.prev = last_node

            """ if there is no next node to head,
            we add new_node as next node to head.
            """
            if self.head.nxt is None:
                self.head.nxt = new_node
                new_node.prev = self.head

            # linking new node to head, will be done in all cases.
            self.head.prev = new_node
            new_node.nxt = self.head

    def traverse(self):
        current = self.head
        print(current.value)
        while current.nxt != self.head:
            print(str(current.nxt.value), ' ')
            current = current.nxt

    def move_head(self):
        next_node = self.head.nxt
        self.head = next_node

    def write_at_head(self, value):
        self.head.value = value


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
                if None != re.search('/api/mult/*', self.path):
                    num1 = float(self.path.split('/')[-1])
                    num2 = float(self.path.split('/')[-2])
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


        with socketserver.ThreadingTCPServer(("", PORT), CustomHandler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()

        


if __name__ == "__main__":
    ss = saveSatistics()
    ss.eventCalled()

        




