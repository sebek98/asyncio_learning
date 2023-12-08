import asyncio

n = 0


async def offset():
    await asyncio.sleep(0)
    return 1


async def increment():
    global n
    n += await offset()   # control goes back to loop


async def safe_increment(lock):
    global n
    await lock.acquire()
    n += await offset()
    lock.release()


async def safe_increment_cm(lock):
    global n
    async with lock:
        n += await offset()


async def main():
    lock = asyncio.Lock()
    tasks = [safe_increment_cm(lock) for i in range(10)]
    await asyncio.gather(*tasks)
    print(n)


asyncio.run(main())
