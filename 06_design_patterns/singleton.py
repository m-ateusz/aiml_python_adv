import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls, model):
        with cls._lock:
            if cls._instance is None:
                print('Creating singleton instance')
                cls._instance = super().__new__(cls)
            print('Returning existing singleton instance')

            return cls._instance
    def __init__(self, model: str) -> None:
        self.model = model

    def work(self):
        print(f'Working...{self.__dict__}')


x = Singleton('test')
x.work()
y = Singleton('dwa')
z = Singleton('trzy')
y.work()
z.work()

print(f'{x is y = } {hex(id(x))=} {hex(id(y))=} {hex(id(z))=}')

