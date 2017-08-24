
import socket
import struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp
phone.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>:').strip()
    if not cmd:continue
    ##发命令
    phone.send(cmd.encode('utf-8'))

    #先收报头
    header=phone.recv(4)
    body_size=struct.unpack('i',header)[0]
    ##再收执行结果

    recv_size=0
    while recv_size < body_size
    cmd_res=phone.recv(1024)
    print(cmd_res.decode('utf-8'))
    # print(cmd_res.decode('gbk'))

phone.close()