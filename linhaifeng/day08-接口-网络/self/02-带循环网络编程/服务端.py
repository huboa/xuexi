##导入模块
import socket,time
###创建连接对象
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) ###复用
#绑定连接tcp
phone.bind(('127.0.0.1',8080))
#监听端口
phone.listen(5)

#等待连接
print('等待连接')
conn,client_addr=phone.accept()
print('已连接')

# print('conn',conn)
# print('client_addr',client_addr)

###基于建立的连接，收发消息
while True:
    print('等待接收信息1024个')
    client_data=conn.recv(1024)
    print("处理信息-变成大写字母",client_data.upper())
    conn.send(client_data.upper())

##关闭连接
conn.close()
###关机、关闭实例
phone.close()
