import socket
import ssl


def server(ipaddr, port, ca_file=None):
    purpose = ssl.Purpose.CLIENT_AUTH
    context = ssl.create_default_context(purpose, cafile=ca_file)
    context.load_default_certs()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ipaddr, port))
    s.listen(1)
    print('Start listening {0} {1}...'.format(ipaddr, port))

    while True:
        conn, addr = s.accept()
        print('Connection from {0}'.format(addr))
        ssl_s = context.wrap_socket(conn, server_side=True)
        ssl_s.send('Welcome connect'.encode())
        while True:
            data = ssl_s.recv(1024)
            if not data:
                break
            print(data.decode())
        ssl_s.close()


if __name__ == '__main__':
    server('127.0.0.1', 12345)
