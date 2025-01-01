from src.adapters.middlewares import get_user_by_request
from src.application.exceptions.unauthorized_exception import Unauthorized
from src.application.exceptions.users.user_must_exists_exception import UserMustExists
from src.domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)


class Delete:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def handler(self, user_id: str) -> dict:
        jwt_data = get_user_by_request.exec()
        if not jwt_data:
            raise Unauthorized()

        if not jwt_data.has_permission(user_id):
            raise Unauthorized()

        user = self.user_repository.destroy_one(user_id)

        if not user:
            raise UserMustExists()

        return {}
