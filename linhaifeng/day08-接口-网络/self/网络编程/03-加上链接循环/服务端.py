import socket,time
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) ###复用
phone.bind(('127.0.0.1',8080))
phone.listen(5)
print('服务ing')
while True:   ###连接循环
    conn,client_addr=phone.accept()
    while True:###基于建立的连接，收发消息
        try:
            client_data=conn.recv(1024)
            if not client_data:break
            print(client_addr)
            conn.send(client_data.upper())
        except Exception:
            break
    conn.close()
phone.close()
