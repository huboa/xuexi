import socketserver

class MyUDPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)
        print(self.client_address)
        self.request[1].sendto(self.request[0].upper(),self.client_address)

if __name__ == '__main__':
    s=socketserver.ThreadingUDPServer(('127.0.0.1',8080),MyUDPhandler)
    s.serve_forever()
