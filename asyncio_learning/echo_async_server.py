import asyncio

async def echo_server(address):
    server = await asyncio.start_server(echo_handler, *address)
    async with server:
        await server.serve_forever()

async def echo_handler(reader, writer):
    while True:
        data = await reader.read(100000)
        if not data:
            break
        writer.write(data)
        await writer.drain()
    print("conn closed")
    writer.close()
    await writer.wait_closed()


if __name__ == "__main__":
    asyncio.run(echo_server(("", 25000)))
