from src.adapters.middlewares import get_user_by_request
from src.application.exceptions.collections.collection_must_be_draft_or_incomplete_exception import (
    CollectionMustBeDraftOrIncomplete,
)
from src.application.exceptions.collections.collection_must_exists_exception import (
    CollectionMustExists,
)
from src.application.exceptions.unauthorized_exception import Unauthorized
from src.domain.core.models.dtos.custom_attribute import CustomAttributesDTO
from src.domain.core.models.value_objects.collection_status import CollectionStatus
from src.domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)


class CustomAtributes:
    def __init__(self, collection_repository: CollectionRepositoryInterface):
        self.collection_repository = collection_repository

    def handler(self, collection_id: str, body: dict) -> dict:

        collection = self.collection_repository.find_by_id(collection_id)

        if not collection:
            raise CollectionMustExists()

        # TODO - Implementar a verificacao de se nao existem itens na colecao
        if not collection.can_add_attributes:
            raise CollectionMustBeDraftOrIncomplete()

        jwt_data = get_user_by_request.exec()

        if jwt_data.id != collection.id and jwt_data.is_admin():
            raise Unauthorized()

        dto = CustomAttributesDTO(**body)

        updated_collection = self.collection_repository.update_custom_attributes(
            collection_id, dto.model_dump()["attributes"], CollectionStatus.INCOMPLETE
        )

        return updated_collection.model_dump()
