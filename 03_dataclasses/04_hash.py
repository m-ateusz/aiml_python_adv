from dataclasses import dataclass, field
"""
Domyślnie dataclasses mają zaimplementowaną metodę __eq__,
ale aby obiekt mógł być umieszczony w zbiorze lub jako klucz
w słowniku, musi być jeszcze zaimplementowana metoda __hash__
"""

@dataclass(frozen=True, kw_only=True, slots=True)
class Point:
    x:int
    y:int = -99

coordinates = { 'y': -20, 'x': -10 }
# coordinates = [10,12]

u1 = Point(**coordinates)

points = set([
    u1,
    Point(x=1,y=1),
    Point(x=-2,y=3),
    Point(x=-1),
    Point(x=3),
])

print(f'{points=} {u1 in points = }')


