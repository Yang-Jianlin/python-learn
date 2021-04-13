import socket

s = socket.socket()

host = socket.gethostname()
port = 45678
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print("Got connect from ", addr)
    message_send = "success connect to " + host
    c.send(message_send.encode())
    c.close()
