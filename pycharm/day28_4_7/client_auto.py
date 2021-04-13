import socket


def client_start(port, ipaddr):
    c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    c1.connect((ipaddr, port))
    while True:
        print('receive info:', c1.recv(1024).decode('utf-8'))
        info = input('enter info:')
        c1.send(info.encode())


if __name__ == '__main__':
    client_start(12345, '127.0.0.1')
