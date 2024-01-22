import os
import asyncio
from time import time
import aiofiles


async def get_python_filename(startdir):
    for root, dirs, files in os.walk(startdir):
        for filename in files:
            if filename.endswith(".py"):
                yield os.path.join(root, filename)


async def producer(q_gen: asyncio.Queue, startdir):
    for root, dirs, files in os.walk(startdir):
        for filename in files:
            if filename.endswith(".py"):
                # print(os.path.join(root, filename))
                await q_gen.put(os.path.join(root, filename))
    await q_gen.put(None)


async def consumer(q_gen: asyncio.Queue, q_cont: asyncio.Queue):
    while True:
        file_path = await q_gen.get()
        if file_path == None:
            await q_gen.put(None)
            await q_cont.put(None)
            return
        async with aiofiles.open(file_path, 'r') as aio_file:
            file_lines = await aio_file.readlines()
            # print(len(file_lines))
        await q_cont.put(len(file_lines))


async def sink(q_cont: asyncio.Queue):
    sum_of_lines = 0
    while True:
        file_lines = await q_cont.get()
        sum_of_lines += file_lines if file_lines is not None else 0
        if file_lines == None:
            print(sum_of_lines)
            return sum_of_lines


async def main():
    loc_sum = 0
    async for file in get_python_filename(r"C:\Users\sburniak\PycharmProjects\asyncio_learning\asyncio_learning"):
        with open(file, 'r') as file:
            # print(f"***** {file} ******")
            loc_sum += len(file.readlines())
    print(loc_sum)


async def main1():
    q_generator = asyncio.Queue()
    q_counter = asyncio.Queue()
    await asyncio.gather(producer(q_generator, r"C:\Users\sburniak\PycharmProjects\asyncio_learning\asyncio_learning"),
                         consumer(q_generator, q_counter),
                         sink(q_counter))



####################################################################################


if __name__ == "__main__":
    # start = time()
    # asyncio.run(main())
    # end = time()
    # print(f"elapsed time {end - start}")
    asyncio.run(main1())
