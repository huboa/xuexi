##买手机
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp

phone.connect(('127.0.0.1',8080))

phone.send('hello upupupup'.encode('utf-8'))
server_data=phone.recv(1024)
print('收到的消息是',server_data)
phone.close()