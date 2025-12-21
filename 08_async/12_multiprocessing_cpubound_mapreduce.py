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
    K, N = params
    while True:
        random_number = random.randint(1, 10 ** 10)
        if md5_check(random_number, K, N):
            print(f"Proces {os.getpid()} znalazł liczbę: {random_number}")
            return random_number


if __name__ == '__main__':
    K = 10000000# 00
    N = 5

    num_processes = 20

    with multiprocessing.Pool(processes=num_processes) as pool:
        # Mapowanie zadań (procesy szukają liczb równocześnie)
        results = pool.map(find_number, [(K, N) for _ in range(num_processes)])

    # Zastosowanie funkcji reduce do znalezienia najmniejszej liczby
    smallest_number = reduce(min, results)

    print(f"Najmniejsza liczba znaleziona przez procesy: {smallest_number}")