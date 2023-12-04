import asyncio


n = 0


async def monitor():
    global n
    while True:
        await asyncio.sleep(1)
        print(f"{n} req/sec")
        n = 0


async def echo_prime_up_to(address):
    global n
    while True:
        reader, writer = await asyncio.open_connection(*address)
        writer.write(b'100')
        await writer.drain()
        resp = await reader.read(100000)
        print(resp)
        # await asyncio.sleep(1)
        n += 1

asyncio.run(echo_prime_up_to(("", 25000)))
# asyncio.get_event_loop().run_until_complete(echo_prime_up_to(("", 25000)))

