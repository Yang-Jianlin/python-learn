import socket
import sys


def server(ipaddr, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ipaddr, port))
    s.listen(1)
    print("Listen at ", s.getsockname())

    while True:
        conn, addr = s.accept()
        conn.sendall('Welcome connect!'.encode())
        print("Connect from {0}".format(addr))

        while True:
            data = conn.recv(1024)
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            conn.sendall(output)
            sys.stdout.flush()

        print()
        conn.close()
        print('Socket close')


if __name__ == '__main__':
    server('127.0.0.1', 12345)
