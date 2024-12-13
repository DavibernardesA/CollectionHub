from application.exceptions.users.user_exception import UserException


class UserMustExists(UserException):
    def __init__(self):
        self.message = ("User must exists", "O usuario deve existir")
        super().__init__()
