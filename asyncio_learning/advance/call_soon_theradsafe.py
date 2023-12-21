import asyncio
import time
import threading


def worker(loop, ev):
    print("worker has started")
    for i in range(10):
        time.sleep(2)
        print("setting alarm!")
        loop.call_soon_threadsafe(ev.set)


async def watcher(ev):
    try:
        print("start watching")
        while True:
            await ev.wait()
            ev.clear()
            print("\nALARM!!!\n")
    except asyncio.CancelledError:
        print("watcher is cancelled")


async def main():
    loop = asyncio.get_running_loop()
    event = asyncio.Event()
    task = asyncio.create_task(watcher(event))
    await asyncio.sleep(0.1)
    th = threading.Thread(target=worker, args=(loop, event))
    th.deamon = True
    th.start()

    await task

asyncio.run(main())