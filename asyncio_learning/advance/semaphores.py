import asyncio


async def run(id, semaphore):
    print(f"{id} waiting for semaphore")
    async with semaphore:
        print(f"{id} is running")
        await asyncio.sleep(1)
        print(f"{id} is done")


async def main():
    semaphore = asyncio.Semaphore(5)
    tasks = [run(i, semaphore) for i in range(10)]
    await asyncio.gather(*tasks)

asyncio.run(main())
