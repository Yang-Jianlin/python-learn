import socket


def create_sock_connect(ipaddr, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ipaddr, port))
    s.listen(1)
    print('Listening at {0} {1}'.format(ipaddr, port))
    accept_sock(s)


def accept_sock(sock):
    while True:
        conn, addr = sock.accept()
        print('Connect from {0}'.format(addr))
        conn.send('Welcome connect!'.encode())
        while True:
            send_message(conn)


def send_message(sock):
    message_lib = {'Beautiful is better than?': 'Ugly',
                   'Explicit is better than?': 'Implicit',
                   'Simple is better than?': 'Complex'}
    message_recv = recv_message(sock, '?')
    for keys in message_lib.keys():
        if message_recv == keys:
            sock.sendall(message_lib[keys].encode())
            break
    else:
        sock.sendall('Error: unknown aphorism.'.encode())


def recv_message(sock, suffix):
    message = sock.recv(1024).decode()
    if not message:
        raise Exception('Socket closed')
    while not message.endswith(suffix):
        data = sock.recv(1024).decode()
        if not data:
            raise Exception('Receive data {0} then socket closed'.format(message))
        message += data
    return message


if __name__ == '__main__':
    create_sock_connect('127.0.0.1', 12345)
