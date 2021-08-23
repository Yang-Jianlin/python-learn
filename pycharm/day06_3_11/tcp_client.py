import time
import socket


def main():
    client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    dst_host = '127.0.0.1'
    dst_port = 12345
    client1.connect((dst_host, dst_port))
    client1.send('Hello'.encode())

    data = client1.recv(1024)
    print(data)

    while True:
        message = "my name is client1"
        client1.send(message.encode())
        time.sleep(1)


if __name__ == '__main__':
    main()
