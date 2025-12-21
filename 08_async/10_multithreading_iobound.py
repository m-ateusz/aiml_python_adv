import threading
import random
import time

def io_bound_task(thread_id, results, lock):
    wait_time = random.randint(2000, 6000)
    time.sleep(wait_time / 1000)

    with lock:
        results.append((thread_id, wait_time))
    print(f"Wątek {thread_id} zakończył zadanie po {wait_time} ms")


def main():
    threads = []
    results = []  # Thread unsafe!
    lock = threading.Lock()  # Blokada dla bezpiecznego dostępu do listy results

    for i in range(50):
        thread = threading.Thread(target=io_bound_task, args=(i, results, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("\nWątki zakończyły działanie w następującej kolejności:")
    for thread_id, wait_time in results:
        print(f"Wątek {thread_id} zakończył po {wait_time} ms")

if __name__ == "__main__":
    main()
