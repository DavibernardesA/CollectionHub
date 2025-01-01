from src.adapters.middlewares import get_user_by_request
from src.application.exceptions.collections.collection_must_exists_exception import (
    CollectionMustExists,
)
from src.application.exceptions.unauthorized_exception import Unauthorized
from src.domain.core.models.value_objects.collection_status import CollectionStatus
from src.domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)


class Detail:
    def __init__(self, collection_repository: CollectionRepositoryInterface) -> None:
        self.collection_repository = collection_repository

    def handler(self, collection_id: str) -> dict:
        collection = self.collection_repository.find_by_id(collection_id)
        if not collection:
            raise CollectionMustExists()

        jwt_data = get_user_by_request.exec()

        if (
            collection.status == CollectionStatus.DELETED
            and jwt_data.id != collection.created_by
        ):
            raise Unauthorized()

        return collection.model_dump()
