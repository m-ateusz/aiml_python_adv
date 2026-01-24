import time

print('1')

from datetime import datetime

def func(a, x = datetime.now()):
    print('2')

    return (a,x)

print(func(1, 111))
time.sleep(1)
print(func(2, 222))
print('3')

print(func(12))
time.sleep(2)
print('4')

print(func(13))

print('5')


