##买手机
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp

phone.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>:').strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))
    cmd_res=phone.recv(1024)
    print('收到的消息是',cmd_res.decode('utf-8'))
phone.close()