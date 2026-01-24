
from typing import TypedDict, Required, NotRequired, Self

class User(TypedDict, total=False):
    firstname: Required[str]
    lastname: Required[str]
    
    age: int
    last_login: int
    spouse: 'User'


# u: User = {'firstname': 'mateusz', 'lastname': 'michael'}
u: User = User(firstname='mateusz', lastname ='michael', age=34)

print(f'{u=} {type(u)=} {type(User)=}')