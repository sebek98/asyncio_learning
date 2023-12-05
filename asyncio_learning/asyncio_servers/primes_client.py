import asyncio


async def echo_prime_up_to(address):
    while True:
        reader, writer = await asyncio.open_connection(*address)
        writer.write(b'100000')
        await writer.drain()
        resp = await reader.read(10000)
        print(resp.decode())
        # await asyncio.sleep(1)

asyncio.run(echo_prime_up_to(("", 25000)))
# asyncio.get_event_loop().run_until_complete(echo_prime_up_to(("", 25000)))

