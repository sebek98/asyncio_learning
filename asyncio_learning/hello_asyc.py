import asyncio
import time


async def hello():
    print("hello start")
    await asyncio.sleep(10)
    print("hello wracam")
    return 1000


async def hello1(n: int = 10) -> int:
    print("hello1 start")
    await asyncio.sleep(n)
    print("hello1 wracam")
    return 100


async def main():
    # asyncio.run(hello())
    # asyncio.run(hello1(1))
    res = await asyncio.gather(hello(), hello1(5))
    return res


if __name__ == "__main__":
    asyncio.run(main())
