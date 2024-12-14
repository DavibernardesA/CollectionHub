from flask import request
from domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from domain.core.models.value_objects.user_type import UserType
from application.exceptions.unauthorized_exception import Unauthorized
from application.utils.paginator import Paginator

class Index:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def handler(self, query_params: dict) -> list:
        if request.user.account_type != UserType.ADMIN:
            raise Unauthorized()

        users = self.user_repository.find_all()

        limit = int(query_params.get("limit", [20])[0])
        page = int(query_params.get("page", [1])[0])

        return Paginator(
            [user.model_dump(exclude_password=True) for user in users],
            limit,
            page
        ).result
