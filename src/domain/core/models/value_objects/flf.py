from enum import Enum


class FLFType(str, Enum):
    FOLLOW = "follow"
    LIKE = "like"
    FAVORITE = "favorite"

    def __str__(self):
        return str(self.value)