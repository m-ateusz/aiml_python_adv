from typing import NamedTuple

class User(NamedTuple):
    firstname: str
    lastname: str
    age: int


# u:User = User('mateusz', 'anonim', 23)
u:User = User(firstname='mateusz', lastname='anonim', age=23)
# u:User = ('mateusz', 'anonim', 23)
u.firstname = 'test'

print(f'{u=} {type(u)=} {type(User)=}')
# print(f'{u.lastname=} {u.age=}')
