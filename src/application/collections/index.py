from application.utils.paginator import Paginator
from domain.core.models.collection import CollectionModel
from domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)


class Index:
    def __init__(self, collection_repository=CollectionRepositoryInterface) -> None:
        self.collection_repository = collection_repository

    def handler(self, query_params: dict) -> list[CollectionModel]:

        collections = self.collection_repository.find_all()

        limit = int(query_params.get("limit", [20])[0])
        page = int(query_params.get("page", [1])[0])

        return Paginator(
            [collection.model_dump() for collection in collections], limit, page
        ).result
