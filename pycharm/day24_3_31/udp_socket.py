import socket
import random


def server(ipaddr, port):
    # 开启UDP服务
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ipaddr, port))
    print('Listening at {0}'.format(s.getsockname()))
    while True:
        data, addr = s.recvfrom(1024)
        print('From {0} Data:{1}'.format(addr, data.decode()))
        info = '12345'
        # 一半的概率会丢失客户端的请求
        if random.random() < 0.5:
            print('Drop packet from {0}'.format(addr))
            continue
        s.sendto(info.encode(), addr)


if __name__ == '__main__':
    server('127.0.0.1', 12345)
