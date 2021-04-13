import socket


def main():
    server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP

    host = '127.0.0.1'
    port = 12345
    server1.bind((host, port))

    server1.listen(5)
    while True:
        conn, addr = server1.accept()
        print("----------------------------")
        print("Success connect from ", addr)
        conn.send("Welcome connect!".encode())

        while True:
            data = conn.recv(1024)
            print("from {0}:".format(addr), data.decode('utf-8'))

        conn.close()


if __name__ == '__main__':
    main()
