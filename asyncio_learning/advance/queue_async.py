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
        if item:
            print(f"consumer {name} got {item}")
        else:
            await q.put(None)   # first consumer takes the None and put another None to queue for the next consumer
            return              # finished the loop with one element (none) in the queue

async def main():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q, "1"), consumer(q, "2"))


if __name__ == "__main__":
    asyncio.run(main())
