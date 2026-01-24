x: int = '123'

if type(x) is not __annotations__['x']:
    x = __annotations__['x'](x)

print(f'{x=} {type(x)=} {__annotations__['x'] = }')

class Test:
    x: int
    y: complex

    def hello(self, name:str) -> None: print(f'hello {name}')

print(f'{Test.__annotations__} {Test.hello.__annotations__=}')