from dataclasses import dataclass
"""
Przykład co się dzieje gdy używamy mutowalnych wartości domyślnych
w definicjach funkcji/metod.

Aby to naprawić należy użyć default_factory

"""
class User:
    login: str
    friends: list[str]

    def __init__(self, login, friends = []):
        self.login = login
        self.friends = friends

alice = User('Alice')
bob = User('Bob')

alice.friends.append('Charlie')
bob.friends.append('Michael')

print(f'{alice.login} knows {", ".join(alice.friends)}.')
print(f'{bob.login} knows {", ".join(bob.friends)}.')


