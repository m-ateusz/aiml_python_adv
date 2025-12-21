import asyncio
import random


async def fetch_data(source_id):
    wait_time = random.randint(2000, 4000)
    await asyncio.sleep(wait_time/1000)
    return f'Dane ze źródła {source_id} po {wait_time} sekundach'


async def main():

    tasks = [fetch_data(i) for i in range(1, 41)]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

if __name__ == '__main__':
    asyncio.run(main())