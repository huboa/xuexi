import socket
sock=socket.socket()
sock.bind("127.0.0.1",8800)
sock.listen(5)
while True:
    print("wating...")
    conn,addr=sock.accept()##默认阻塞
    data=conn.recv(1024)
    print('data',data)
    conn.send(b"")