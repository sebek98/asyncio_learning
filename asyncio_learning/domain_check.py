import asyncio
import socket
from keyword import kwlist


async def test(addr: str):
    loop = asyncio.get_running_loop()
    try:
        await loop.getaddrinfo(addr, None)
        print(f"Domena {addr} istnieje")
    except socket.gaierror as e:
        print(f"Domena {addr} nie istnieje")

async def sleeper(n: int):
    print(f"zaczynam {n}")
    await asyncio.sleep(n)
    print(f"Koncze {n}")
    return n

async def main1():
    coros = [sleeper(3), sleeper(5), sleeper(9), sleeper(1)]
    for coro in asyncio.as_completed(coros):
        res = await coro


async def main():
    domains = [f"{d}.pl".lower() for d in kwlist]
    tests_func = [test(d) for d in domains]
    # await asyncio.gather(*tests_func)
    for coro in asyncio.as_completed(tests_func):
        await coro


asyncio.run(main1())
