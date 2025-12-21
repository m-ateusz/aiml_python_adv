class Account:
    login: str

    def __init__(self, login):
        self.login = login

class User(Account):
    pass

class Admin(Account):
    pass

class Guest(Account):
    pass

user = User('mateusz')
admin = Admin('admin')
guest = Guest('guest')

print(f'{isinstance(user, User) = }')
print(f'{isinstance(user, Account) = }')
print(f'{isinstance(user, object) = }')
print(f'{isinstance(user, Guest) = }')