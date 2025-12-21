class User:
    first_name: str
    def __init__(self, first_name: str) -> None:
        self.first_name = first_name


user = User('Mateusz')
print(f'{isinstance(user, User) = }')
print(f'{isinstance(user, object) = }')
print(f'{isinstance(user, type) = }')