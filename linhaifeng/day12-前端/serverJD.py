import socket
sock=socket.socket()
sock.bind("127.0.0.1",8080)
sock.listen(5)
while True:
    print("wating...")
    conn,addr=sock.accept() ##默认阻塞
    data=conn.recv(1024)
    print('data',data)
    conn.send(b"HTTP/1.1 201 OK \r\n \r\n <h1>hello<h1\>")
    conn.close()
