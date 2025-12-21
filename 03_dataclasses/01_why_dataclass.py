from dataclasses import dataclass
"""
Przykład przydatności dataclasses, 
w celu zmiany klasy Point z 2D na 3D należy wykonać sporo pracy...

"""
class Point:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        else:
            return NotImplemented


print(f'{Point(1.0, 2.0)}')