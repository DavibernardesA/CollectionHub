from src.application.exceptions.flf.flf_exception import (
    FLFException
)


class FLFAMustExists(FLFException):
    def __init__(self):
        self.message = ("Action must exists", "A ação deve existir")
        super().__init__()
