import socket
import time


def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = input('enter info:')
    s.sendto(info.encode(), ('127.0.0.1', 59657))


if __name__ == '__main__':
    server()
