import asyncio
import time


async def async_counter(n):
    while n > 0:
        await asyncio.sleep(0.2)
        yield n
        n -= 1


def counter(n):
    while n > 0:
        time.sleep(0.2)
        yield n
        n -= 1


class Counter:
    def __init__(self, n):
        self.n = n

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.n >= 0:
            await asyncio.sleep(0.2)
            self.n -= 1
            return self.n
        else:
            raise StopAsyncIteration


async def main():
    async for n in async_counter(10):
        print(n)

    # for n in counter(10):
    #     print(n)


if __name__ == "__main__":
    asyncio.run(main())