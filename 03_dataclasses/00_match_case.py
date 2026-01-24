from dataclasses import dataclass

@dataclass()
class Point:
    x: float
    y: float

l = [
    Point(-1,2),
    Point(1,2),
    Point(0,0),
    2+3j
]
x = 2.0

for p in l:
    match p:
        # case Point():
        #     print(f'{p=} jest punktem')
        case Point(0,a):
            print(f'CASE #1: {p=} {a=}')
        case Point(1, 2):
            print(f'CASE #3: {p=}')
        case Point(test, x) if test > 0:
            print(f'CASE #2: {p=} {test=} {x=}')

        case _:
            print('coś innego')

