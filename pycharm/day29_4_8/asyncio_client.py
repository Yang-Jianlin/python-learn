import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    while True:
        send_info = input('enter info:')
        writer.write(send_info.encode())

        while True:
            data = await reader.read(100)
            if not data:
                break
            print('Received: %r' % data.decode())

        writer.close()


while True:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_echo_client())
