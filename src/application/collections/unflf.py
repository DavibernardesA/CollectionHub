from src.adapters.middlewares import get_user_by_request
from src.application.exceptions.collections.collection_must_exists_exception import (
    CollectionMustExists,
)
from src.application.exceptions.unauthorized_exception import Unauthorized
from src.domain.core.models.value_objects.collection_status import CollectionStatus
from src.domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)
from src.domain.core.models.value_objects.flf import FLFType
from src.application.exceptions.invalid_credentials_exception import InvalidCredentials
from src.domain.core.ports.repositories.flf_collection_repository_interface import FLFColllectionRepositoryInterface
from src.application.exceptions.flf.flf_action_must_exists import FLFAMustExists

class UnFLF:
    def __init__(self, collection_repository: CollectionRepositoryInterface, flf_collection_repository: FLFColllectionRepositoryInterface) -> None:
        self.collection_repository = collection_repository
        self.flf_collection_repository = flf_collection_repository

    def handler(self, collection_id: str, query_params: dict, body: dict) -> dict:
        collection = self.collection_repository.find_by_id(collection_id)
        if not collection:
            raise CollectionMustExists()

        if collection.status == CollectionStatus.DELETED:
            raise Unauthorized()

        action = query_params.get("action", [None])[0]
        if not action or action not in [item.value for item in FLFType]:
            raise InvalidCredentials()

        jwt_data = get_user_by_request.exec()

        flf = self.flf_collection_repository.find_by_id_and_action(jwt_data.id, action)
        if not flf:
            raise FLFAMustExists()

        self.flf_collection_repository.delete(account_id=jwt_data.id, action=action)
        self.collection_repository.recive_action(collection_id=collection.id, action=action, negative=True)

        return {}
