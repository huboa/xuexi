import socket
#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#插卡
phone.bind(('127.0.0.1',8080))
#开机
phone.listen(5)
#等电话链接
print('server start...')
conn,client_addr=phone.accept() #(tcp链接,client_addr)
print('链接',conn)
print(client_addr)

#基于建立的链接，收发消息
client_data=conn.recv(1024)
print('客户端的消息',client_data)
conn.send(client_data.upper())

#挂电话链接
conn.close()

#关机
phone.close()