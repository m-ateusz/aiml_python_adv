from typing import Callable


def hi() -> int:
    print('hi')
    return 0

def hello(name) -> str:
    print(f'Hello {name}')
    return f'Hello {name}'


class User:
    firstname: str
    lastname: str

x:Callable[[], int] = hi

x()

class Test:
    def hello(self) -> None: # Callable[ [Test] ,None]
        print('hello world')

test: Test = Test()

y:Callable[[], None] = test.hello