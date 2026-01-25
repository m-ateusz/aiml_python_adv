import asyncio

async def task(name, duration, fail=False):
    print(f"Zadanie {name} rozpoczęte.")
    await asyncio.sleep(duration)
    if fail:
        raise ValueError(f"Błąd w zadaniu {name}!")
    print(f"Zadanie {name} zakończone.")
    return f"Wynik {name}"

async def main():
    try:
        results = await asyncio.gather(
            task("A", 2),
            task("B", 3, fail=True),  # To zadanie rzuci wyjątek
            task("C", 1),
            return_exceptions=True
        )
        print("\nWyniki:", results)
    except Exception as e:
        print("\nBłąd:", e)

asyncio.run(main())
