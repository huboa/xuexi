##买手机
import socket
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp
##udp


#插卡
phone.bind('127.0.0.1',8080)
#开机
phone.listen(5)

#等电话
conn,client_addr=phone.accept()

###基于建立的连接，收发消息
client_data=conn.recv(1024)
conn.send(client_data.upper())



##挂电话
conn.close()
###关机
phone.close()