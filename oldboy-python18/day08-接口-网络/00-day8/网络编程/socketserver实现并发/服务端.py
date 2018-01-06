import socketserver
class MyTcphandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True: #通信循环
            data=self.request.recv(1024)
            self.request.send(data.upper())
if __name__ == '__main__':
    #取代链接循环
    server=socketserver.ThreadingTCPServer(('127.0.0.1',8080),MyTcphandler)
    server.serve_forever()