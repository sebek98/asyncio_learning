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


async def main():
    domains = [f"{d}.pl".lower() for d in kwlist]
    tests_func = [test(d) for d in domains]
    # await asyncio.gather(*tests_func)
    for coro in asyncio.as_completed(tests_func):
        await coro


asyncio.run(main())
