import asyncio
import contextlib

@contextlib.contextmanager
def simple_cm(param):
    print("cm enter")
    try:
        yield param
    finally:
        print("cm exit")

@contextlib.asynccontextmanager
async def tcp_client(host, port):
    reader, writer = await asyncio.open_connection(host, port)
    try:
        yield reader, writer
    finally:
        writer.close()
        await writer.wait_closed()


async def main():
    with simple_cm("something") as s:
        print(s)
        print("inside cm")

    async with tcp_client("google.com", 80) as (reader, writer):
        print("inside async cm")
        writer.write(b"GET / HTTP/1.0\r\n\r\n")
        await writer.drain()
        data = await reader.read(1000)
        print(data)



asyncio.run(main())
