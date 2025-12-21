import multiprocessing
import time
import random


def worker(semaphore):
    with semaphore:
        print(f'Worker {multiprocessing.current_process().name} is working...')
        time.sleep(random.uniform(500, 4000)/1000)  # Symulacja pracy
        print(f'Worker {multiprocessing.current_process().name} done.')

if __name__ == '__main__':
    semaphore = multiprocessing.Semaphore(2)  # Max 2 procesy jednocześnie
    processes = [multiprocessing.Process(target=worker, args=(semaphore,)) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
