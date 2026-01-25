import asyncio
import itertools
import time
from time import sleep


async def long_task():
    print("Zadanie rozpoczęte...")

    # await asyncio.sleep(5)
    # time.sleep(5)
    for i in itertools.count(1):
        await asyncio.sleep(0)
        time.sleep(0.3)
        print('.', end='')
    print("Zadanie zakończone!")
    return "Wynik zadania"

async def main():
    try:
        result = await asyncio.wait_for(long_task(), timeout=2)
        print(f"Zadanie zwróciło: {result}")
    except asyncio.TimeoutError:
        print("Timeout! Zadanie trwało zbyt długo i zostało anulowane.")

asyncio.run(main())
