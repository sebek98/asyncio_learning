import asyncio
import time


async def echo_client(address):
    while True:
        reader, writer = await asyncio.open_connection(*address)
        writer.write(b"Hello from async client")
        await writer.drain()
        resp = await reader.read(100000)
        print(b'got: ' + resp)
        await asyncio.sleep(1)

asyncio.run(echo_client(("", 25000)))