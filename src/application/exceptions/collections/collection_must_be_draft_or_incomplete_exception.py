from src.application.exceptions.collections.collections_exception import (
    CollectionsException,
)


class CollectionMustBeDraftOrIncomplete(CollectionsException):
    def __init__(self):
        self.message = (
            "Collection must be draft or incomplete",
            "A coleção deve estar em rascunho ou incompleta",
        )
        super().__init__()
