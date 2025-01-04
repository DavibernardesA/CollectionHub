from src.adapters.middlewares import get_user_by_request
from src.application.exceptions.collections.collection_must_exists_exception import (
    CollectionMustExists,
)
from src.application.exceptions.unauthorized_exception import Unauthorized
from src.domain.core.models.value_objects.collection_status import CollectionStatus
from src.domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)
from src.domain.core.ports.repositories.lock_repositpory_interface import (
    LockRepositoryInterface,
)


class Delete:
    def __init__(
        self,
        collection_repository: CollectionRepositoryInterface,
        lock_repository: LockRepositoryInterface,
    ):
        self.collection_repository = collection_repository
        self.lock_repository = lock_repository

    def handler(self, collection_id: str, body: dict) -> dict:
        collection = self.collection_repository.find_by_id(collection_id)

        if not collection:
            raise CollectionMustExists()

        jwt_data = get_user_by_request.exec()

        if not jwt_data.id != collection.created_by:
            raise Unauthorized()

        if not collection.can_delete:
            raise Unauthorized()

        # esse lock serve para garantir que não sera possivel deletar uma collection enquanto adiciona um item
        self.lock_repository.lock(collection.id)

        self.collection_repository.delete(
            status=CollectionStatus.DELETED, collection_id=collection_id
        )

        if self.lock_repository.find_by_collection_id(collection.id):
            self.lock_repository.unlock(collection.id)

        return {}
