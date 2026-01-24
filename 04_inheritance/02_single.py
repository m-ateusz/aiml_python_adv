class Account:
    login: str

    def __init__(self, login):
        self.login = login

    def hello(self):
        print(f'Hello {self.__class__.__name__} {self.login} {self.comment}!')

class User(Account):
    comment: str
    def __init__(self, login, comment='test'):
        super().__init__(login)
        self.comment = comment
        self.__class__.__name__ = 'TERT'

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

user.hello()
# guest.hello()