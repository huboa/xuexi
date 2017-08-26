from socket import *
udp_server=socket(AF_INET,SOCK_DGRAM)
udp_server.bind(('127.0.0.1',8080))


data1,client_addr=udp_server.recvfrom(1)
print('data1',data1)

data2,client_addr=udp_server.recvfrom(1024)
print('data2',data2)