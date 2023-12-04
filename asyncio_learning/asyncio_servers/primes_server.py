import asyncio
import time


async def echo_server(address):
    server = await asyncio.start_server(primes_server, *address)
    async with server:
        await server.serve_forever()


async def primes_server(reader, writer):
    while True:
        data = await reader.read(10000)
        prime_to_test = int(data.decode())
        primes = primes_up_to(prime_to_test)
        writer.write(f"{primes}\n".encode("utf-8"))
        await writer.drain()


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes_up_to(n):
    result = []
    for i in range(n+1):
        if is_prime(i):
            result.append(i)
    return result


if __name__ == "__main__":
    asyncio.run(echo_server(("", 25000)))
