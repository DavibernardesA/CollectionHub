from src.domain.core.models.item import ItemModel

from src.domain.core.ports.repositories.collection_repository_interface import CollectionRepositoryInterface
from src.domain.core.ports.repositories.item_repository_interface import ItemRepositoryInterface
from src.application.exceptions.collections.collection_must_exists_exception import (
    CollectionMustExists,
)
from src.adapters.middlewares import get_user_by_request
from src.application.utils.paginator import Paginator

class Index:
    def __init__(self, item_repository: ItemRepositoryInterface, collection_repository: CollectionRepositoryInterface):
        self.item_repository = item_repository
        self.collection_repository = collection_repository

    def handler(self, collection_id: str, query_params: dict) -> list[ItemModel]:
        
        collection = self.collection_repository.find_by_id(collection_id)

        if not collection:
            raise CollectionMustExists()
        
        items = self.item_repository.find_items_by_collection(collection.id) or []

        jwt_data = get_user_by_request.exec()

        items = list(
            item for item in items
            if item.visibility or item.is_visible_to_user(jwt_data, collection)
        )

        limit = int(query_params.get("limit", [20])[0])
        page = int(query_params.get("page", [1])[0])

        return Paginator(
           [item.model_dump() for item in items], limit, page
        ).result
