import asyncio


async def handle_echo(reader, writer):
    while True:
        data = await reader.read(100)
        if data:
            message = data.decode()
            ipaddr = writer.get_extra_info('peername')
            print("Received {0} from {1}".format(message, ipaddr))

            re_info = 'received ' + message
            writer.write(re_info.encode())
            await writer.drain()
        else:
            break


loop = asyncio.get_event_loop()
co_connect = asyncio.start_server(handle_echo, '127.0.0.1', 8888, loop=loop)
server = loop.run_until_complete(co_connect)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
