from socket import *
from multiprocessing import Process
s=socket(AF_INET,SOCK_STREAM)
s.bind('127.0.0.1',8080)
s.listen(5)


def talk(conn,addr):
    while True:
        try:
            data=conn.recv(1024)
            if not data:break
            conn.send(data.upper())
        except Exception:
            break
    conn.close()
if __name__ == '__main__':
    while True:
        conn,addr=s.accept()
        p=Process(target=talk,args=(conn,addr))
        p.start()
    s.close()