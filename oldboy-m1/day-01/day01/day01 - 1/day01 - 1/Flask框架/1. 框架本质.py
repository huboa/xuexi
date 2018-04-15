import socket

def main():
    # 创建老师
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.listen(5)

    while True:
        # 老师等待 用户请求的到来
        connection, address = sock.accept()
        # 获取发送的内容：alex有没有女朋友？
        # 获取发送的内容：ni 有没有女朋友？
        # 获取发送的内容：石鹏有没有女朋友？
        # 获取发送的内容：吴亦凡有没有女朋友？
        buf = connection.recv(1024)

        # 根据请求URL的不同：
        # 回答：没有
        connection.send(b"HTTP/1.1 200 OK\r\n\r\n")
        connection.send(b"No No No")

        # 关闭连接
        connection.close()


if __name__ == '__main__':
    main()