import asyncio
from concurrent.futures import ProcessPoolExecutor


pool = ProcessPoolExecutor(max_workers=8)

async def echo_server(address):
    server = await asyncio.start_server(echo_handler, *address)
    async with server:
        await server.serve_forever()


async def echo_handler(reader, writer):
    while True:
        data = await reader.read(10000)
        try:
            prime_to_test = int(data)
        except ValueError:
            continue
        ## code CPU invensive here - not working, blocking the loop
        #1
        # res = primes_up_to(prime_to_test)
        #2
        # res = await asyncio.to_thread(primes_up_to, prime_to_test)
        #3
        #
        loop = asyncio.get_running_loop()
        res = await loop.run_in_executor(pool, primes_up_to, prime_to_test)
        ## CPU intensive was there
        writer.write(f"{res}\n".encode("utf-8"))
        await writer.drain()
    print("conn closed")
    writer.close()
    await writer.wait_closed()


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
