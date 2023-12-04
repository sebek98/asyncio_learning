import asyncio
import time


# 1
async def echo_client(address):
    reader, writer = await asyncio.open_connection(*address)
    for i in range(20):
        writer.write(str(i).encode())
        await writer.drain()
        resp = await reader.read(100000)
        to_str = resp.decode()
        print(f"{i} jest pierwsza: {resp.decode()}")
        await asyncio.sleep(0.25)


asyncio.run(echo_client(("", 25000)))
