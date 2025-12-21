from dataclasses import dataclass, field

"""
Co zrobić jeśli chcemy uniemożliwić tworzenie punktów o ujemnych współrzędnych?
"""

@dataclass
class Point:
    x: int
    y: int

points = [
    Point(x=1, y=2),
    Point(x=-3, y=-4),
]

