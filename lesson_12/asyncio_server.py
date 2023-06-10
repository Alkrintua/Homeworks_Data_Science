import asyncio

async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        message = data.decode().strip()

        if message == 'quit':
            writer.close()
            break

        try:
            operation, num1, num2 = message.split()
            num1 = int(num1)
            num2 = int(num2)

            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            else:
                result = 'Unknown operation'

            response = str(result).encode()
            writer.write(response)
            await writer.drain()
        except Exception as e:
            error_message = str(e)
            writer.write(error_message.encode())
            await writer.drain()

async def main():
    server = await asyncio.start_server(
        handle_client, 'localhost', 50000)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()

asyncio.run(main())