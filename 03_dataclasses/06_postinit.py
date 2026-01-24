from dataclasses import dataclass, field, fields
from datetime import datetime

"""
Co zrobić jeśli chcemy uniemożliwić tworzenie punktów o ujemnych współrzędnych?
"""
LIMIT_X = [0,3]

@dataclass(kw_only=True, unsafe_hash=True)
class Point:

    x: int = field(default=0, metadata={'units': 'cm', 'limit': LIMIT_X})
    y: int = field(default=0, metadata={'units': 'cm', 'limit': [0,10]})
    comment: str = field(init=False, default="Default comment", repr=False)
    as_complex:complex = field(init=False, repr=False, compare=False)
    timestamp: datetime = field(init=False, default_factory=datetime.now)
    done: bool = field(init=False, default=False, repr=False, compare=False, hash=False)


    def __post_init__(self):
        if self.x < 0 or self.y < 0:
            raise ValueError('Point must be non-negative.')
        self.as_complex = complex(self.x, self.y)
        limit_x = fields(self)[0].metadata['limit']
        limit_y = fields(self)[1].metadata['limit']

        if not (limit_x[0] <= self.x <= limit_x[1]):
            raise ValueError(f'Point must be between {limit_x}.')
        if not (limit_y[0] <= self.y <= limit_y[1]):
            raise ValueError(f'Point must be between {limit_y}.')
        self.done = True

    def __setattr__(self, name, value):
        if self.done:
            raise ValueError
        object.__setattr__(self, name, value)

    def __add__(self, other):
        # Tak nie robimy!
        # self.x += other.x
        # self.y += other.y

        # Robimy tak
        return Point(x=self.x + other.x, y=self.y + other.y)



points = [
    Point(x=1, y=2),
    Point(y=3),
    Point(x=2),
    # Point(x=-3, y=-4),
]
# points[1].comment = 'New comment'
print(f'{points=}')

for point in points:
    print(f'{point.as_complex=}')

print(f'{points[0] + points[1]=}')

