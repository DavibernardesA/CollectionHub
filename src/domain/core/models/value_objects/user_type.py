from enum import Enum


class UserType(str, Enum):
    ADMIN = "admin"
    USER = "user"

    def __str__(self):
        return str(self.value)
