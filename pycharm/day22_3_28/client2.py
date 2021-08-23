import socket


def client_start(port, ipaddr):
    c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c2.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    c2.connect((ipaddr, port))
    while True:
        print('receive info:', c2.recv(1024).decode('utf-8'))
        info = input('enter info:')
        c2.send(info.encode())


if __name__ == '__main__':
    client_start(12345, '127.0.0.1')
