import socket
import random
import sys


def client(ipaddr, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # ipaddr = sys.argv[2]
    s.connect((ipaddr, port))
    print('The os assigned me the address {0}'.format(s.getsockname()))

    delay = 0.1
    send_data = '1234567'
    while True:
        s.send(send_data.encode())
        print('waiting up to {0} seconds for a reply'.format(delay))
        s.settimeout(delay)
        try:
            data = s.recv(1024)
            print('Data:{0}'.format(data.decode()))
        except socket.timeout:
            delay *= 2
            if delay > 2.0:
                raise RuntimeError('I think the server is down')
            else:
                continue


if __name__ == '__main__':
    client('127.0.0.1', 12345)
