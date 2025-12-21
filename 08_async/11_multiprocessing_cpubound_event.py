import multiprocessing
import hashlib
import random
import os
from functools import reduce

def md5_check(num, K, N):
    hash_object = hashlib.md5(str(num).encode())
    md5_hash = hash_object.hexdigest()

    return (int(md5_hash, 16) % K) < N

def find_number(params):
    K, N, stop_event = params
    counter = 0
    while True:
        counter += 1
        if counter % 1000 == 0:  # Check stop_event every 1000 iterations
            if stop_event.is_set():
                return 10 ** 10

        random_number = random.randint(1, 10 ** 10)
        if md5_check(random_number, K, N):
            print(f"Proces {os.getpid()} znalazł liczbę: {random_number}")
            stop_event.set()
            return random_number
    return 10 ** 10

if __name__ == '__main__':
    K = 100000000
    N = 5

    num_processes = 20

    # Use a manager to create a shared stop event
    with multiprocessing.Manager() as manager:
        stop_event = manager.Event()

        with multiprocessing.Pool(processes=num_processes) as pool:
            # Map tasks (processes search for numbers concurrently)
            results = pool.map(find_number, [(K, N, stop_event) for _ in range(num_processes)])

        # Use reduce to find the smallest number
        smallest_number = reduce(min, results)

        print(f"liczba znaleziona przez procesy: {smallest_number}")
