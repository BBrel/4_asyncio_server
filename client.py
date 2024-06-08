import asyncio


class EchoClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def send_message(self, message):
        reader, writer = await asyncio.open_connection(
            self.host, self.port)

        print(f'Send: {message}')
        writer.write(message.encode())

        data = await reader.read(100)
        print(f'Received: {data.decode()}')
        writer.close()
        await writer.wait_closed()


# Запуск клиента и отправка сообщения
client = EchoClient('127.0.0.1', 8888)
asyncio.run(client.send_message('Hello World!'))
