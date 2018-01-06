from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',8080))
s.listen(5)

conn,addr=s.accept()

#收发消息
data1=conn.recv(5)
print('data1:',data1)

data2=conn.recv(5)
print('data2',data2)


conn.close()
s.close()





