import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))


phone.send('hello'.encode('utf-8'))
server_data=phone.recv(1024)
print('服务端回应的消息',server_data)

phone.close()