import socket
import ssl


def client(ipaddr, port, ca_file=None):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose, cafile=ca_file)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ipaddr, port))
    ssl_s = context.wrap_socket(s, server_hostname=ipaddr)
    data = ssl_s.recv(1024)
    print(data)
    while True:
        message = input('enter info:')
        ssl_s.sendall(message.encode())


if __name__ == '__main__':
    client('127.0.0.1', 12345)
