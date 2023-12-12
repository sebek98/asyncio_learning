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
    shielded_task = asyncio.shield(task)
    await asyncio.sleep(1)
    shielded_task.cancel()
    await task


asyncio.run(main_sigle_coro())
