from dataclasses import dataclass, field
"""
Domyślnie dataclasses mają zaimplementowaną metodę __eq__,
ale to nie wystarcza do ustanowienia porządku liniowego
"""
@dataclass(order=True)
class User:
    login: str

@dataclass(order=True)
class Point:
    x:int
    y:int
    owner: User

points = [
    Point(0,0, User('qadmin')),
    Point(1,1, User('admin')),
    Point(-2,3, User('service')),
    Point(0,0, User('guest')),
    Point(0,-5, User('mateusz')),
]

print(f'{min(points)=}')
print(f'{max(points)=}')
print(f'{sorted(points)=}')