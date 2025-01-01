import os

from src.application.exceptions.invalid_credentials_exception import InvalidCredentials
from src.application.exceptions.users.user_already_exists_exception import UserAlreadyExists
from src.domain.core.models.dtos.create_user import CreateUser
from src.domain.core.models.value_objects.user_type import UserType
from src.domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)


class Create:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def handler(self, body: dict) -> dict:
        body["account_type"] = (
            UserType.ADMIN
            if body.get("password_admin") == os.getenv("ADMIN_PASS")
            else UserType.USER
        )

        if body.get("password_admin") and body["account_type"] == UserType.USER:
            raise InvalidCredentials()

        dto = CreateUser(**body)
        if self.user_repository.find_by_email(dto.email):
            raise UserAlreadyExists()

        created_user = self.user_repository.insert_one(dto)
        return created_user.model_dump()
