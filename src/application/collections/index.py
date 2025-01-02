from src.application.utils.paginator import Paginator
from src.domain.core.models.collection import CollectionModel
from src.domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)
from src.domain.core.models.value_objects.collection_status import CollectionStatus


class Index:
    def __init__(self, collection_repository: CollectionRepositoryInterface) -> None:
        self.collection_repository = collection_repository

    def handler(self, query_params: dict) -> list[CollectionModel]:

        status = query_params.get("status", CollectionStatus.DELETED)[0]

        collections = self.collection_repository.find_all(status)

        limit = int(query_params.get("limit", [20])[0])
        page = int(query_params.get("page", [1])[0])

        return Paginator(
            [collection.model_dump() for collection in collections], limit, page
        ).result
