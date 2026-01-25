import multiprocessing
import time
import random

def increment_value(shared_value, lock):
    name = f'Thread-{random.randint(1,100)}'
    for _ in range(5):
        # time.sleep(random.uniform(500, 2000)/1000)
        with lock:
            x = shared_value.value
            time.sleep(random.uniform(1, 2) / 5000)
            shared_value.value = x+1
            print(f'Updated value: {shared_value.value} {name=}')

if __name__ == '__main__':

    shared_value = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    processes = []

    for _ in range(5):
        p = multiprocessing.Process(target=increment_value, args=(shared_value, lock))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f'Final value: {shared_value.value}')
