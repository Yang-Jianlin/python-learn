import socket
import threading


class ServerThread:
    def __init__(self, ipaddr, port, num):
        self.ipaddr = ipaddr
        self.port = port
        self.num = num

    def server_link(self, conn, addr):
        conn.send("Welcome connect!".encode())

        while True:
            try:
                data = conn.recv(1024)
                if data:
                    print("from {0}:".format(addr), data.decode('utf-8'))
                else:
                    break
            except Exception:
                break

        conn.close()

    def server_start(self):
        s_pro = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s_pro.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_pro.bind((self.ipaddr, self.port))
        s_pro.listen(self.num)
        print('Waiting link...')
        while True:
            conn, addr = s_pro.accept()
            print("Success connect from ", addr)
            p = threading.Thread(target=self.server_link, args=(conn, addr))
            p.start()


if __name__ == '__main__':
    server = ServerThread('127.0.0.1', 12345, 5)
    server.server_start()
