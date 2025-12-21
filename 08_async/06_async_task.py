import asyncio

async def coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")

async def main():
    print("Task is about to be run")
    task = asyncio.create_task(coroutine())
    await asyncio.sleep(0.5)
    print("Task was run")

    await task
    print('----------------- now coroutine ')

    print("Coroutine is about to be run")
    task = coroutine()
    await asyncio.sleep(0.5)
    print("Coroutine was run")
    await task

asyncio.run(main())