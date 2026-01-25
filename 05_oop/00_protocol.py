from typing import Protocol


class Testable(Protocol):
    def test(self): ...

class Test:
    x: int
    y: int
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __enter__(self):
        print(f"wchodzę {self} {self.x} {self.y}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"exit: {exc_type}, {exc_val}, {exc_tb} ")

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def raise_exception(self):
        raise ValueError('Ejże!')

    def __iter__(self):
        return self

    def __lt__(self, other):
        if isinstance(other, Test) and self.x < other.x:
            return True
        else:
            return False

    def test(self): print(self)


class X(Test):
    pass

with Test(1,2) as test:
    print(f"{test=}")
    # test.raise_exception()

t1 = Test(0,0)
t2 = Test(1,1)

print(f'{t1 < t2 = }')

t3:Testable = X(0,0)
t3.test()
