import asyncio

async def send_request(reader, writer, request):
    writer.write(request.encode())
    await writer.drain()

    data = await reader.read(100)
    response = data.decode().strip()
    print("Response:", response)

async def main():
    reader, writer = await asyncio.open_connection('localhost', 50000)

    await send_request(reader, writer, "add 5 3")
    await send_request(reader, writer, "subtract 10 2")
    await send_request(reader, writer, "multiply 7 4")

    writer.write("quit".encode())
    await writer.drain()

    writer.close()
    await writer.wait_closed()

asyncio.run(main())