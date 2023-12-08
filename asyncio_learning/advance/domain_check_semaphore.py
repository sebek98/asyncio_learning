import asyncio
import socket
from keyword import kwlist


async def test(addr: str, semaphore: asyncio.Semaphore):
    print(f"{addr} waiting for semaphore")
    loop = asyncio.get_running_loop()
    async with semaphore:
        print(f"{addr} działa")
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


async def test_ascomplete():
    coros = [sleeper(3), sleeper(5), sleeper(9), sleeper(1)]
    for coro in asyncio.as_completed(coros):
        await coro


async def main():
    semaphore = asyncio.Semaphore(2)
    domains = [f"{d}.pl".lower() for d in kwlist]
    tests = [test(dom, semaphore) for dom in domains]
    res = await asyncio.gather(*tests)

    print("done")


# asyncio.run(test_ascomplete())
asyncio.run(main())
