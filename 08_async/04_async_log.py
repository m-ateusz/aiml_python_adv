import asyncio
import random
import time

async def fetch_data(source_id):
    print(f'[{source_id:04d}] started!')
    wait_time = random.randint(50, 500)
    print(f'[{source_id:04d}] przed sleep: {wait_time}')
    await asyncio.sleep(wait_time/1000)

    # time.sleep(wait_time/1000)
    print(f'[{source_id:04d}] po sleep')
    return source_id

async def main():
    tasks = [fetch_data(i) for i in range(1, 11)]
    # tasks = []
    # tasks.append(fetch_data(0)
    # tasks.append(fetch_data(1)
    # tasks.append(fetch_data(2)
    # ...

    # tasks = [obj_awaitable...]
    print(f'[main] Przed gather!')
    results = await asyncio.gather(*tasks)

    for item in results:
        print(item)
if __name__ == '__main__':
    asyncio.run(main())