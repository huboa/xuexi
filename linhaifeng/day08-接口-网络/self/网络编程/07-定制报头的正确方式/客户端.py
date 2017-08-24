import socket
import struct
import json
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    #发命令
    phone.send(cmd.encode('utf-8'))


    #先收报头的长度
    struct_res=phone.recv(4)
    print(struct_res)
    header_size=struct.unpack('i',struct_res)[0]
    print(header_size)

    #再收报头
    header_bytes=phone.recv(header_size)
    print(header_bytes)
    head_json=header_bytes.decode('utf-8')
    head_dic=json.loads(head_json)

    total_size=head_dic['total_size']
    #再收命令的执行结果
    recv_size=0
    data=b''
    while recv_size < total_size:
        recv_data=phone.recv(1024)
        recv_size+=len(recv_data)
        data+=recv_data

    #打印结果
    # print(data.decode('gbk'))
    print(data.decode('utf-8'))
phone.close()