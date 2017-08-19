##买手机
import socket,time

phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp

#插卡
phone.bind(('127.0.0.1',8080))
#开机
phone.listen(5)

#等电话
print('等待电话')
conn,client_addr=phone.accept()
print('连接')
print(conn,client_addr)


###基于建立的连接，收发消息
while True:##通话交流
    client_data=conn.recv(1024)
    print('客户信息')
    print(client_data.upper())
    conn.send(client_data.upper())



##挂电话
conn.close()
###关机
phone.close()
