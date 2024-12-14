from application.exceptions.users.user_must_exists_exception import UserMustExists
from domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)


class Detail:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def handler(self, user_id: str) -> dict:
        user = self.user_repository.find_by_id(user_id)

        if not user:
            raise UserMustExists()

        return user.model_dump(exclude_password=True)
