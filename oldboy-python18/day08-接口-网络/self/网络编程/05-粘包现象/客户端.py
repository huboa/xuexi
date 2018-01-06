from socket import *
import time
c=socket(AF_INET,SOCK_STREAM)
c.connect(('127.0.0.1',8080))


c.send('hello'.encode('utf-8'))
# time.sleep(3)
c.send('world'.encode('utf-8'))


c.close()
