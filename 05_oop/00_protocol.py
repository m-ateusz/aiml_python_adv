class Test:
    x: int
    y: int
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __enter__(self):
        print(f"wchodzę {self} {self.x} {self.y}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"exit: {exc_type}, {exc_val}, {exc_tb} ")



with Test(1,2) as test:
    print(f"{test=}")