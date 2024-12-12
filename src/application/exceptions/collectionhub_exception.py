from settings import LANGUAGE

class CollectionHubException(Exception):
    def __init__(self, message, error_type):
        super().__init__()
        self.message = message
        self.error_type = error_type

    def to_dict(self):
        message = self.message[1] if LANGUAGE == "pt" else self.message[0]
        data = {
            "id": "validation_failed",
            "message": self.message[0],
            "meta": {"errors": {self.error_type: message}},
        }
        return data
