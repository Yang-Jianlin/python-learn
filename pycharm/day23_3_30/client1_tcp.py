import socket


class Client1:
    def __init__(self, ipaddr, port):
        self.ipaddr = ipaddr
        self.port = port

    def client_link(self):
        c1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c1.connect((self.ipaddr, self.port))
        # print('receive info:', c1.recv(1024).decode('utf-8'))
        while True:
            info = input('enter info:')
            c1.send(info.encode())


if __name__ == '__main__':
    c = Client1('127.0.0.1', 8888)
    c.client_link()
