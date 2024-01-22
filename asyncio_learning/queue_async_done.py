import asyncio


async def producer(q: asyncio.Queue):
    for i in range(10):
        await q.put(f"task {i}")
        print(f"produced task {i}")
        await asyncio.sleep(0.1)
    await q.put(None)


async def consumer(q: asyncio.Queue, name):
    while True:
        item = await q.get()
        print(f"consumer {name} got {item}")
        await asyncio.sleep(0.5)
        q.task_done()


async def main():
    q = asyncio.Queue()
    p = asyncio.create_task(producer(q))
    consumers = asyncio.gather(consumer(q, "1"), consumer(q, "2"))
    await p
    print(f"producer has finished")
    await q.join()
    print(f"q is exhausted")
    consumers.cancel()
    try:
        await consumers
    except asyncio.CancelledError:
        print("consumers are cancelled")


if __name__ == "__main__":
    asyncio.run(main())
