import asyncio
import time
import threading


def worker(loop):
    print("worker has started")
    time.sleep(2)
    print("running courutine")
    future = asyncio.run_coroutine_threadsafe(some_coro(), loop)
    print("waiting for courutine")
    future.result()
    print("finish worker")


async def some_coro():
    print("I am a courutine")
    await asyncio.sleep(1)


async def main_work():
    await asyncio.sleep(4)


async def main():
    loop = asyncio.get_running_loop()
    await asyncio.sleep(0.1)
    task = loop.create_task(main_work())
    th = threading.Thread (target=worker, args=(loop,))
    th.deamon = True
    th.start()

    await task
    th.join()

asyncio.run(main())