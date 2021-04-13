import socket
from multiprocessing import Process


class ServerProcess:
    def __init__(self, ipaddr, port, num):
        self.ipaddr = ipaddr
        self.port = port
        self.num = num

    # 服务端的数据接收，在调用时使用多进程
    def server_link(self, conn, addr):
        conn.send("Welcome connect!".encode())

        while True:
            try:
                data = conn.recv(1024)
                if data:
                    print("from {0}:".format(addr), data.decode('utf-8'))
                else:
                    break
            except Exception:
                break

        conn.close()

    # 服务端的启动程序
    def server_start(self):
        # IPv4
        s_pro = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口
        s_pro.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_pro.bind((self.ipaddr, self.port))
        s_pro.listen(self.num)
        print('Waiting link...')
        while True:
            conn, addr = s_pro.accept()
            print("Success connect from ", addr)
            # 启动多进程实现多连接
            p = Process(target=self.server_link, args=(conn, addr))
            p.start()


if __name__ == '__main__':
    server = ServerProcess('127.0.0.1', 12345, 5)
    server.server_start()
