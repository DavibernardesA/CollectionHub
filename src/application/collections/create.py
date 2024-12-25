from domain.core.ports.repositories.collection_repository_interface import CollectionRepositoryInterface
from domain.core.ports.repositories.user_repository_interface import UserRepositoryInterface

from application.exceptions.collections.collection_already_exists_exception import CollectionAlreadyExists

from domain.core.models.dtos.create_collection import CreateCollection
from adapters.middlewares import get_user_by_request
from application.exceptions.unauthorized_exception import Unauthorized
from domain.core.models.value_objects.collection_status import CollectionStatus


class Create:
    def __init__(self, collection_repository: CollectionRepositoryInterface, user_repository: UserRepositoryInterface) -> None:
        self.collection_repository = collection_repository
        self.user_repository = user_repository

    def handler(self, body: dict) -> dict:
        body["status"] = CollectionStatus.DRAFT

        jwt_data = get_user_by_request.exec()
        if not jwt_data or not self.user_repository.find_by_id(jwt_data.id):
            raise Unauthorized()

        body["created_by"] = jwt_data.id

        dto = CreateCollection(**body)

        if self.collection_repository.find_by_name(dto.name):
            raise CollectionAlreadyExists()

        created_collection = self.collection_repository.insert_one(dto)
        return created_collection.model_dump()
