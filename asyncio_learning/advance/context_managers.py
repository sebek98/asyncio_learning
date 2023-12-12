import asyncio


class AsyncContextManager:
    def __init__(self, param):
        self.param = param

    async def __aenter__(self):
        print(f"{self.param} __aenter__")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.param} __aexit__")

    async def proceed(self):
        await asyncio.sleep(1)
        print(f"{self.param} proceed")


async def main():
    with open("context_managers.py") as f:
        print(f.read())

    async with AsyncContextManager("something") as s:
        await s.proceed()



asyncio.run(main())
