from socket import *
import socketserver

class MyUDPhandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.request)


if __name__ == '__main__':

udp_server=socket(AF_INET,SOCK_DGRAM)

udp_server.bind(('127.0.0.1',8080))

