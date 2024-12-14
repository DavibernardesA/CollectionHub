from flask import request
from domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from domain.core.models.value_objects.user_type import UserType
from application.exceptions.unauthorized_exception import Unauthorized

class Destroy:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def handler(self, user_id: str) -> dict:
        if request.user.id != user_id or request.user.account_type != UserType.ADMIN:
            raise Unauthorized()

        user = self.user_repository.destroy_one(user_id)

        if not user:
            raise Unauthorized(("User not found or already deleted.", "Usuario nao encontrado ou ja foi deletado"))

        return {}