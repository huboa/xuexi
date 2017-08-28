from socket import *
udp_server=socket(AF_INET,SOCK_DGRAM)

udp_server.bind(('127.0.0.1',8080))

while True:
    data,client_addr=udp_server.recvfrom(1024)
    print(data,client_addr)
    udp_server.sendto(data.upper(),client_addr)