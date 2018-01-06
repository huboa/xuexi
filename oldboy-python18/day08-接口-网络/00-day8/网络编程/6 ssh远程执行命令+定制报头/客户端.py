import socket
import struct
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    #发命令
    phone.send(cmd.encode('utf-8'))


    #先收报头
    header=phone.recv(4)
    total_size=struct.unpack('i',header)[0]

    #再收命令的执行结果
    recv_size=0
    data=b''
    while recv_size < total_size:
        recv_data=phone.recv(1024)
        recv_size+=len(recv_data)
        data+=recv_data

    #打印结果
    print(data.decode('gbk'))

phone.close()