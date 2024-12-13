from application.exceptions.users.user_exception import UserException


class UserAlreadyExists(UserException):
    def __init__(self):
        self.message = ("User already exists", "O usuario ja existe")
        super().__init__()
