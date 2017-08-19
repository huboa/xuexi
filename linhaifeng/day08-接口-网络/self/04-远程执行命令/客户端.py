##买手机
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp

phone.connect(('127.0.0.1',8080))

while True:
    msg=input('>>:').strip()
    if not msg:continue
    phone.send(msg.encode('utf-8'))
    server_data=phone.recv(1024)
    print('收到的消息是',server_data.decode('utf-8'))
phone.close()