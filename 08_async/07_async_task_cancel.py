import asyncio

async def long_task():
    try:
        print("Task started...")
        await asyncio.sleep(10)
        print("Task finished!")
    except asyncio.CancelledError:
        print("Task was cancelled!")
    print("I don't care")


async def main():
    task = asyncio.create_task(long_task())
    await asyncio.sleep(3)
    print("Cancelling task...")
    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Handled task cancellation in main")
    print("Main function finished.")


asyncio.run(main())
