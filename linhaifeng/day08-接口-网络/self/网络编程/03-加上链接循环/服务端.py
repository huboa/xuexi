import socket,time
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) ###复用
phone.bind(('127.0.0.1',8080))
phone.listen(5)
print('启动服务')
while True:   ###连接循环
    conn,client_addr=phone.accept()
    ###基于建立的连接，收发消息
    while True:##通话交流
        try:
            client_data=conn.recv(1024)
            if not client_data:break###针对对linux
            print('客户信息')
            print(client_data.upper())
            conn.send(client_data.upper())
        except Exception: ##针对windows
            break

    ##挂电话
    conn.close()
###关机
phone.close()
