import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
phone.bind(('127.0.0.1',8080))
phone.listen(5)
print('server start...')
while True: #链接循环
    conn,client_addr=phone.accept()
    print(conn,client_addr)

    while True: #通讯循环
        try:
            client_data=conn.recv(1024)
            if not client_data:break #针对linux系统
            # print('has rev')
            conn.send(client_data.upper())
        except Exception: #针对windwos
            break
    conn.close()

phone.close()