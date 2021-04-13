import socket


def main():
    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    dst_host = '127.0.0.1'
    dst_port = 12345
    client1.connect((dst_host, dst_port))
    client1.send('Hello'.encode())

    while True:
        data = client1.recv(1024)
        print("from ('127.0.0.1', 12345):", data)
        message = input("client send:")
        client1.send(message.encode())


if __name__ == '__main__':
    main()
