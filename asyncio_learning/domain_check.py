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


async def test_ascomplete():
    coros = [sleeper(3), sleeper(5), sleeper(9), sleeper(1)]
    for coro in asyncio.as_completed(coros):
        await coro


async def main():
    domains = [f"{d}.pl".lower() for d in kwlist]
    # 1
    # tests_func = [test(d) for d in domains]
    # await asyncio.gather(*tests_func)  # podstawowe zadanie: zwraca rezultat wszystkich

    # 2
    # tests_func = [test(d) for d in domains]
    # for coro in asyncio.as_completed(tests_func):
    #     await coro                        # zwraca wszystkie w kolejności w jakiej się skonczyły

    # 3
    tests_func = [asyncio.create_task(test(d)) for d in domains]
    done, pending = await asyncio.wait(tests_func, return_when=asyncio.FIRST_COMPLETED)
    for task in done:
        print(task.result())
    for task in pending:
        task.cancel()
    print("done")


# asyncio.run(test_ascomplete())
asyncio.run(main())
