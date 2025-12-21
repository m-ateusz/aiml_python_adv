import asyncio
import random
import time

async def fetch_data(source_id):
    print(f'{source_id} started!')
    wait_time = random.randint(50, 500)
    # await asyncio.sleep(wait_time/1000)
    time.sleep(wait_time/1000)
    response = f'Dane ze źródła {source_id} po {wait_time} milisekundach'
    print(f'{response=}')
    return response


async def main():

    tasks = [fetch_data(i) for i in range(1, 11)]
    # tasks = []
    # tasks.append(fetch_data(0)
    # tasks.append(fetch_data(1)
    # tasks.append(fetch_data(2)
    # ...

    # tasks = [obj_awaitable...]
    print(f'Przed gather!')
    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

if __name__ == '__main__':
    asyncio.run(main())