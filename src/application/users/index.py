from domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from application.utils.paginator import Paginator

class Index:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def handler(self, query_params: dict) -> list:

        users = self.user_repository.find_all()

        limit = int(query_params.get("limit", [20])[0])
        page = int(query_params.get("page", [1])[0])

        return Paginator(
            [user.model_dump(exclude_password=True) for user in users],
            limit,
            page
        ).result
