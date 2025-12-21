from dataclasses import dataclass, field
"""
Domyślnie dataclasses mają zaimplementowaną metodę __eq__,
ale aby obiekt mógł być umieszczony w zbiorze lub jako klucz
w słowniku, musi być jeszcze zaimplementowana metoda __hash__
"""

@dataclass
class Point:
    x:int
    y:int


points = set([
    Point(0,0),
    Point(1,1),
    Point(-2,3),
    Point(-1,4),
    Point(3,5),
])

