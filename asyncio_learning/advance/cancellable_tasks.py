import asyncio

async def coro(delay):
    print(f"coro({delay})")
    try:
        await asyncio.sleep(delay)
    except asyncio.CancelledError:
        print(f"coro cancelled")
    else:
        print(f"coro({delay}) done")


async def main_sigle_coro():
    print("launching coro")
    task = asyncio.create_task(coro(5))
    await asyncio.sleep(2)
    task.cancel()
    await task


async def main_multiple_coro():
    coros = [coro(i) for i in range(1,5)]
    print("launching coro")
    tasks = asyncio.gather(*coros) # this is a task which creates courutines
    await asyncio.sleep(1)
    tasks.cancel()
    try:
        await tasks
    except asyncio.CancelledError:
        print("Gather task is cancelled")


asyncio.run(main_multiple_coro())