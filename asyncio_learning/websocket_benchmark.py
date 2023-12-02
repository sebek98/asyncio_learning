import asyncio
import websockets


async def client1():
  async with websockets.connect('ws://localhost:8080') as websocket:
    message = 'client 1!'
    await websocket.send(message)
    while True:
      response = await websocket.recv()
      await websocket.send(message)


async def client2():
    async with websockets.connect('ws://localhost:8080') as websocket:
        message = 'client 2!'
    while True:
        response = await websocket.recv()
        await websocket.send(message)


async def main():
    task1 = asyncio.create_task(client1())
    task2 = asyncio.create_task(client2())
    await asyncio.gather(task1, task2)

asyncio.run(main())
