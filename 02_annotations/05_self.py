from typing import Self

class User:
    login: str
    deputy: set['User']

class Admin(User):
    pass # deputy: set[Admin]

user = User()
friend_admin = Admin()

admin = Admin()
admin.deputy = {user, friend_admin}
