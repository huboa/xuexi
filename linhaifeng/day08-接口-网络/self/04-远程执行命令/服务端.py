##买手机
import socket
import subprocess

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) ###复用
#插卡
phone.bind(('127.0.0.1',8080))
#开机
phone.listen(5)

#等电话
while True:   ###连接循环
    print('等待电话')
    conn,client_addr=phone.accept()
    print('连接')
    print(conn,client_addr)


    ###基于建立的连接，收发消息
    while True:##通话交流
        try:
            cmd_data=conn.recv(1024)
            if not cmd_data:break###针对对linux
            print('客户信息')
            res=subprocess.Popen(cmd.decode('utf-8'))
                


            conn.send(client_data.upper())
        except Exception: ##针对windows
            break


    ##挂电话
    conn.close()
###关机
phone.close()
