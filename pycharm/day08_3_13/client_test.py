import socket
import time


class Client1:
    def __init__(self, dst_host, dst_port, buf_size):
        self.dst_host = dst_host
        self.dst_port = dst_port
        self.buf_size = buf_size

        # 参数表示选择TCP/IP协议族，使用TCP 协议创建套接字
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 操作系统会在客户端socket被关闭或客户端进程终止后马上释放该客户端的端口
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 连接目标服务器
        self.client.connect((self.dst_host, self.dst_port))

    def send_message(self):
        message = "111"
        self.client.send(message.encode())

    def recv_message(self):
        data = self.client.recv(self.buf_size)
        print("from ('{0}', {1}):".format(self.dst_host, self.dst_port), data.decode())


if __name__ == '__main__':
    n = 0
    while True:
        port = [12345, 23456]
        c = Client1('127.0.0.1', port[n], 1024)
        if n == len(port)-1:
            n = 0
        else:
            n = n+1
        c.recv_message()

        c.send_message()

        c.client.close()
        print(n)
        time.sleep(1)
