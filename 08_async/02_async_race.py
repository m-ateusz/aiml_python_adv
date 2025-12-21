import asyncio
import random

async def increment_value(shared_value, lock):
    name = f'Task-{random.randint(1,100)}'
    for _ in range(5):
        await asyncio.sleep(random.uniform(0.2, 0.5))
        # async with lock:
        x = shared_value['value']
        await asyncio.sleep(random.uniform(0.1, 0.2))
        shared_value['value'] = x + 1
        print(f'Updated value: {shared_value["value"]} {name=}')

async def main():
    shared_value = {'value': 0}
    lock = asyncio.Lock()

    tasks = []
    for _ in range(10):
        task = asyncio.create_task(increment_value(shared_value, lock))
        tasks.append(task)

    await asyncio.gather(*tasks)
    print(f'Final value: {shared_value["value"]}')

if __name__ == '__main__':
    asyncio.run(main())
