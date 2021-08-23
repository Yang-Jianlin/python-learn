import socket


def main():
    client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    dst_host = '127.0.0.1'
    dst_port = 12345
    client2.connect((dst_host, dst_port))
    client2.send('Hello'.encode())

    data = client2.recv(1024)
    print(data)

    while True:
        flag = int(input("coming(0/1)?"))
        if flag == 1:
            message = input("send:")
            client2.send(message.encode())
        else:
            break


if __name__ == '__main__':
    main()
