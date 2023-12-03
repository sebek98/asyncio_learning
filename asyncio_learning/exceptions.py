import asyncio


async def coro(delay, crash):
    print(f"will sleep for {delay}")
    await asyncio.sleep(delay)
    print("finish waiting")
    if crash:
        raise ValueError
    return 42

async def main():
    try:
        await coro(1, True)
    except ValueError:
        print("Error handled")


async def main_gather_default():
    tasks = [coro(5, False), coro(3, True)]
    try:
        res = await asyncio.gather(*tasks)
        print(res)
    except ValueError:
        print("Error handled")


async def main_gather_with_exceptions():
    tasks = [coro(5, False), coro(3, True)]
    t = asyncio.gather(*tasks, return_exceptions=True)
    res = await t
    print(res)


#taski sa bardziej elastyczne bo przy asyncio.wait dostajemy liste taskow z ktorymi mozemy "cos" zrobic
#w przykladzie wyzej potrzebowalismy tego przelacznika 'return exceptions'
#domyslne zachowanie asyncio.wait to: ALL_COMPLETED
async def main_wait():
    coro1 = [coro(3, False), coro(5, True)]
    tasks = [asyncio.create_task(c) for c in coro1]
    done, pending = await asyncio.wait(tasks)
    for task in done:
        try:
            res = await task
            print(res)
        except ValueError:
            print("error occured")

async def main_wait_with_all_completed():
    coro1 = [coro(3, False), coro(2, True), coro(5, True)]
    tasks = [asyncio.create_task(c) for c in coro1]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED, timeout=4)
    for task in done:
        try:
            res = await task
            print(res)
        except ValueError:
            print("error occured")
    print(f"pending: {pending}")

async def main_wait_with_timeout():
    coro1 = [coro(3, False), coro(2, True), coro(5, True)]
    tasks = [asyncio.create_task(c) for c in coro1]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION, timeout=4)
    for task in done:
        try:
            res = await task
            print(res)
        except ValueError:
            print("error occured")
    print(f"pending: {pending}")
    print(len(pending))


asyncio.run(main_wait_with_timeout())