import asyncio
from itertools import starmap


async def task(name, duration):
    print(f"Zadanie {name} rozpoczęte.")
    await asyncio.sleep(duration)
    print(f"Zadanie {name} zakończone.")
    return f"Wynik {name}"

async def main():
    tasks = list(map(asyncio.create_task, [task("A", 2), task("B", 5), task("C", 3)]))
    done, pending = await asyncio.wait(tasks, timeout=3)

    print("\nZadania zakończone:")
    for t in done:
        print(await t)

    print("Still pending")
    for item in pending:
        print(await item)

asyncio.run(main())
