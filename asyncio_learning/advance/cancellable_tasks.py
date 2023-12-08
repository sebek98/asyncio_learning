import asyncio

async def coro(delay):
    print(f"coro({delay})")
    try:
        await asyncio.sleep(delay)
    except asyncio.CancelledError:
        print(f"coro cancelled")
    else:
        print(f"coro({delay}) done")


async def main():
    # coros = [coro(i) for i in range(1,5)]
    print("launching coro")
    task = asyncio.create_task(coro(5))
    await asyncio.sleep(2)
    task.cancel()
    await task


asyncio.run(main())