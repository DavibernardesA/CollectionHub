from application.exceptions.collections.collection_must_exists_exception import (
    CollectionMustExists,
)
from domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)


class Detail:
    def __init__(self, collection_repository: CollectionRepositoryInterface) -> None:
        self.collection_repository = collection_repository

    def handler(self, collection_id: str) -> dict:
        collection = self.collection_repository.find_by_id(collection_id)
        if not collection:
            raise CollectionMustExists()

        return collection.model_dump()
