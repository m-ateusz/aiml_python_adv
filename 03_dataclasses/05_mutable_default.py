from dataclasses import dataclass, field
"""
Przykład co się dzieje gdy używamy mutowalnych wartości domyślnych
w definicjach funkcji/metod.

Aby to naprawić należy użyć default_factory

"""
@dataclass
class User:
    login: str
    friends: list[str] = field(default_factory=list)

    # domyślna impl __init__

    def __post_init__(self):
        if self.login != self.login.lower():
            raise ValueError('login must be lowercase')





alice = User('alice')
bob = User('bob')

alice.friends.append('charlie')
bob.friends.append('michael')

print(f'{alice.login} knows {", ".join(alice.friends)}.')
print(f'{bob.login} knows {", ".join(bob.friends)}.')

daniel = User('daniel')
print(f'{daniel.login} knows {", ".join(daniel.friends)}.')


