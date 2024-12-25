from application.exceptions.collections.collections_exception import CollectionsException

class CollectionMustExists(CollectionsException):
    def __init__(self):
        self.message = ("Collection must exists", "A coleção deve existir")
        super().__init__()