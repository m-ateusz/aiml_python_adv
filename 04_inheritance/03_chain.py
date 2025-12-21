class Account:
    login: str

    def __init__(self, login):
        self.login = login

class User(Account):
    pass

class Admin(User):
    pass

class Guest(Account):
    pass

user = User('mateusz')
admin = Admin('admin')
guest = Guest('guest')

print(f'{isinstance(user, Admin) = }')
print(f'{isinstance(user, User) = }')
print(f'{isinstance(user, Account) = }')
print(f'{isinstance(user, object) = }')
print(f'{isinstance(user, Guest) = }')

print(f'{isinstance(admin, Admin) = }')
print(f'{isinstance(admin, User) = }')
print(f'{isinstance(admin, Account) = }')
print(f'{isinstance(admin, object) = }')
print(f'{isinstance(admin, Guest) = }')