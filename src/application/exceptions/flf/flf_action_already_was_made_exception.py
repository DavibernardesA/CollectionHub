from src.application.exceptions.flf.flf_exception import (
    FLFException
)


class FLFActionWasMade(FLFException):
    def __init__(self):
        self.message = ("Action already was made", "A ação ja foi feita")
        super().__init__()
