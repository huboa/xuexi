from socket import *
udp_client=socket(AF_INET,SOCK_DGRAM)
while True:
    msg=input('>>：').strip()
    udp_client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))
    data,server_addr=udp_client.recvfrom(1024)
    print(data.decode('utf-8'))