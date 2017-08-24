from socket import *
s=socket(AF_INET,SOCK_STREAM)
s.bind('127.0.0.1',8080)
s.listen(5)
conn,addr=s.accept()

##收消息


conn.close()
s.close()