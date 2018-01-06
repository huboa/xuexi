import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #就是它，在bind前加
phone.bind(('127.0.0.1',8080))
phone.listen(5)
print('server start...')
conn,client_addr=phone.accept()

while True: #通讯循环
    client_data=conn.recv(1024)
    # print('has rev')
    conn.send(client_data.upper())

conn.close()

phone.close()