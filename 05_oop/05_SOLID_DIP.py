class PostgresDB:
   def insert_user(self, name: str) -> None:
       print(f"INSERT INTO users ... ({name})")

class UserService:
   def __init__(self):
       self.db = PostgresDB()  # twarda zależność

   def register(self, name: str) -> None:
       self.db.insert_user(name)

