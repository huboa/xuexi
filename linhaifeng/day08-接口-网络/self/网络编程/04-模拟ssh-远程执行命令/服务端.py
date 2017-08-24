####建立连接
import socket
import subprocess
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) ###复用
phone.bind(('127.0.0.1',8080))
phone.listen(5)

while True:   ###连接循环
    conn,client_addr=phone.accept()
    print(conn,client_addr)

    ###基于建立的连接，收发消息
    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd:break  ###针对对linux异常断开就跳出
            print('客户信息')
            res=subprocess.Popen(cmd.decode('utf-8'),
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            stdout=res.stdout.read()
            stderr=res.stderr.read()


            conn.send(stdout+stderr)
        except Exception: ##针对windows异常跳出
            break


    ##挂电话
    conn.close()
###关机
phone.close()
