import socket

s = socket.socket()

host = socket.gethostname()
port = 45678

s.connect((host, port))
print(s.recv(45678))


