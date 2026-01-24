from dataclasses import dataclass
from typing import Any, Callable
"""
Przykład przydatności dataclasses, 
w celu zmiany klasy Point z 2D na 3D należy wykonać sporo pracy...

"""
@dataclass
class User:
    login: str
    deputy: set['User']


@dataclass
class Point:
    x: float
    y: float
    z: float # 1
    owner: User

    def length(self):
        return (self.x**2 + self.y ** 2 + self.z)**0.5

u1 = Point(1.0, 2.0, 3.0, User('mateusz', set()))
u2 = Point(1.0, 2.0, 3.0, User('mateusz', set()))

print(f'{u1 = } {u2 = } {u1==u2 = }')

# print(f'{hash(u1)=} {hash(u2)=} {id(u1)=} {id(u2)=}')
#
# print({u1, u2})