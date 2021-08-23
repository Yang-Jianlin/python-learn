import socket


class Server1:
    def __init__(self, host, port, lst_num):
        self.host = host
        self.port = port
        self.lst_num = lst_num

        # 参数表示选择TCP/IP协议族，使用TCP协议创建套接字
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定ip和端口
        self.server.bind((self.host, self.port))

        self.server.listen(self.lst_num)  # 最多连接几个客户端
        print("---------Server start!---------")
        # 等待客户端连接连接，如果客户端连接，就会获取到客户端套接字连接和客户端地址
        self.conn, self.addr = self.server.accept()
        print("Success connect from ", self.addr)
        self.conn.send("Welcome connect!".encode())

    def send_message(self, conn):
        message = input("server send:")
        conn.send(message.encode())

    def recv_message(self, conn, addr):
        data = conn.recv(1024)
        print("from {0}:".format(addr), data.decode('utf-8'))


if __name__ == '__main__':
    while True:  # 循环开启服务端服务，等待多个客户端的连接
        s = Server1('127.0.0.1', 12345, 5)

        '''循环对一个客户端接收消息;
        若是一个客户端异常断开，用try except捕获异常，
        防止服务端程序终止，不影响继续等待其他客户端连接。'''
        while True:
            try:
                s.recv_message(s.conn, s.addr)
            except Exception:
                break

        s.conn.close()  # 关闭一个客户端的连接
        s.server.close()  # 关闭套接字
