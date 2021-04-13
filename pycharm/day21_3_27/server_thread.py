import socket
import threading


def server_link(conn, addr):
    conn.send("Welcome connect!".encode())

    while True:
        data = conn.recv(1024)
        if data:
            print("from {0}:".format(addr), data.decode('utf-8'))
        else:
            break

    conn.close()


def server_start(port, ipaddr, lis_num):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ipaddr, port))
    s.listen(lis_num)
    print('Waiting link...')
    while True:
        conn, addr = s.accept()
        print("----------------------------")
        print("Success connect from ", addr)
        t = threading.Thread(target=server_link, args=(conn, addr,))
        t.start()


if __name__ == '__main__':
    server_start(12345, '127.0.0.1', 5)
