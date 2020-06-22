import asyncio

async def endless_func(loop):
    while True:
        print(loop.time())
        await asyncio.sleep(0.1)

async def endless_func2():
    while True:
        print('2')
        await asyncio.sleep(0.01)

loop = asyncio.get_event_loop()

loop.create_task(endless_func(loop))
loop.create_task(endless_func2())

loop.run_forever()