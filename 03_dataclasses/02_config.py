from dataclasses import dataclass

"""
Problem z sortowaniem obiektów, czy wrzucaniem ich do słownika
"""

@dataclass
class Person:
    name: str
    age: int


people = set([
    Person('John', 18),
    Person('Joe', 19),
    Person('Alice', 17),
    Person('Bob', 28),
    Person('Charlie', 25),
])

print(sorted(people))