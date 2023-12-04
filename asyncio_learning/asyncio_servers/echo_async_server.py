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
        data = int(data.decode())
        res = is_prime(data)
        to_b = str(res).encode()
        writer.write(to_b)
        await writer.drain()
    print("conn closed")
    writer.close()
    await writer.wait_closed()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    asyncio.run(echo_server(("", 25000)))
