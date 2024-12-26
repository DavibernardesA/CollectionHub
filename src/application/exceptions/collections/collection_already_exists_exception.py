from application.exceptions.collections.collections_exception import (
    CollectionsException,
)


class CollectionAlreadyExists(CollectionsException):
    def __init__(self):
        self.message = ("Collection already exists", "A coleção ja existe")
        super().__init__()
