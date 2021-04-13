import socket
import sys


def client(ipaddr, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ipaddr, port))

    with open('Bigdata.txt', 'r') as file:
        message = file.read()
    s.sendall(message.encode())
    sys.stdout.flush()

    receive = 0
    while True:
        data = s.recv(42)
        if not receive:
            print('The first data receive says', repr(data))
        if not data:
            break
        receive += len(data)
        print('\r %d bytes received' % (receive,), end=' ')

    print('-------------')
    s.close()


if __name__ == '__main__':
    client('127.0.0.1', 12345)
