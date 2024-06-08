import asyncio


class EchoServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def handle_echo(self, reader, writer):
        data = await reader.read(100)
        message = data.decode()
        addr = writer.get_extra_info('peername')

        print(f"Received '{message}' from {addr}")
        writer.write(data)
        await writer.drain()

        print("Close the connection")
        writer.close()

    async def start_server(self):
        server = await asyncio.start_server(
            self.handle_echo, self.host, self.port)

        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()


# Запуск сервера
server = EchoServer('127.0.0.1', 8888)
asyncio.run(server.start_server())
