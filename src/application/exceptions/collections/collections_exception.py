from application.exceptions.collectionhub_exception import CollectionHubException


class CollectionsException(CollectionHubException):
    error_type = "collections"
    message = None

    def __init__(self):
        super().__init__(self.message, self.error_type)
