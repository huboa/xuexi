####建立连接
import socket
import struct
import subprocess
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)###tcp
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) ###复用
phone.bind(('127.0.0.1',8080))
phone.listen(5)
print('server start...')
while True:   ###连接循环
    conn,client_addr=phone.accept()
    print(conn,client_addr)

    ###基于建立的连接，收发消息
    while True:
        try:
            cmd=conn.recv(1024)
            if not cmd:break  ###针对对linux异常断开就跳出
            print('cmd',cmd)
            res=subprocess.Popen(cmd.decode('utf-8'),
                                 shell=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE)
            stdout=res.stdout.read()
            stderr=res.stderr.read()

            ##先发报头（固定长度）
            header=struct.pack('i',len(stdout)+len(stderr))
            conn.send(header)
            ##再发真实数据
            conn.send(stdout)
            conn.send(stderr)




        except Exception: ##针对windows异常跳出
            break


    ##挂电话
    conn.close()
###关机
phone.close()
