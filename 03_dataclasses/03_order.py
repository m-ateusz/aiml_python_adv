from dataclasses import dataclass, field
"""
Domyślnie dataclasses mają zaimplementowaną metodę __eq__,
ale to nie wystarcza do ustanowienia porządku liniowego
"""

@dataclass
class Point:
    x:int
    y:int


points = [
    Point(0,0),
    Point(1,1),
    Point(-2,3),
    Point(-1,4),
    Point(3,5),
]

print(f'{min(points)=}')
print(f'{max(points)=}')
print(f'{sorted(points)=}')