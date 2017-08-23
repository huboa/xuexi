import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.connect(('127.0.0.1',8080))

while True:
    cmd=input('>>: ').strip()
    if not cmd:continue
    #发命令
    phone.send(cmd.encode('utf-8'))

    #收命令的执行结果
    cmd_res=phone.recv(1024)

    #打印结果
    print(cmd_res.decode('gbk'))

phone.close()