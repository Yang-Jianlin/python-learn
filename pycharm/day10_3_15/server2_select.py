import select
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('127.0.0.1', 23456))
server.listen(5)
inputs = [server]

while True:
    rs, ws, es = select.select(inputs, [], [])
    for r in rs:
        if r == server:
            conn, addr = server.accept()
            print("Success connect from ", addr)
            conn.send("Welcome connect!".encode())
            inputs.append(conn)
        else:
            try:
                data = r.recv(1024)
                print(data.decode('utf-8'))
            except Exception as info:
                inputs.remove(r)
                print(info)
