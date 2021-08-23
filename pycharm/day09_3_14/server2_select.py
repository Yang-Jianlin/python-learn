import socket
import select


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
        self.inputs = [self.server]
        print("---------Server start!---------")
        self.conn = 0
        self.addr = 0

    def send_message(self, conn):
        message = input("server send:")
        conn.send(message.encode())

    def recv_message(self, conn, addr):
        data = conn.recv(1024)
        print("from {0}:".format(addr), data.decode('utf-8'))


if __name__ == '__main__':
    s = Server1('127.0.0.1', 62121, 5)
    while True:  # 循环开启服务端服务，等待多个客户端的连接
        rs, ws, es = select.select(s.inputs, [], [])
        for r in rs:
            if r == s.server:
                conn, addr = s.server.accept()
                print("Success connect from ", addr)
                conn.send("Welcome connect!".encode())
                s.inputs.append(conn)
            else:
                try:
                    s.recv_message(r, )
                except Exception as info:
                    s.inputs.remove(r)
                    print(info)
