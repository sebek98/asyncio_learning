import asyncio


class AsyncFile:

    def __init__(self, filename):
        self.filename = filename
        # self.file = None

    async def __aenter__(self):
        self.file = open(self.filename)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # can be blocking
        await asyncio.to_thread(self.file.close)

    async def __aiter__(self):
        for line in self.file:
            if not line: break
            yield line

    async def __anext__(self):
        pass

    async def read(self):
        # can be blocking
        return await asyncio.to_thread(self.file.read)


async def main():
    async with AsyncFile("async_file_manager.py") as f:
        content = await f.read()
        print(content)


if __name__ == "__main__":
    asyncio.run(main())
