from src.application.exceptions.collectionhub_exception import CollectionHubException


class FLFException(CollectionHubException):
    error_type = "flf"
    message = None

    def __init__(self):
        super().__init__(self.message, self.error_type)
