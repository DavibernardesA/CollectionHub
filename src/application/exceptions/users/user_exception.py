from application.exceptions.collectionhub_exception import CollectionHubException


class UserException(CollectionHubException):
    error_type = "user"
    message = None

    def __init__(self):
        super().__init__(self.message, self.error_type)
