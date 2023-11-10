
class UserService:
    def __init__(self, database):
        self.database = database

    def get_user_by_id(self, user_id):
        user = self.database.get_user_by_id(user_id)
        return user

