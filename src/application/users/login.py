import os
from domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from domain.core.models.dtos.login_user import LoginUser
from application.exceptions.invalid_credentials_exception import InvalidCredentials
from datetime import datetime, timedelta, timezone
from jwt import encode


class Login:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def handler(self, body: dict) -> dict:
        dto = LoginUser(**body)
        user = self.user_repository.find_by_email(dto.email)
        if not user or not user.password_check(dto.password, user.password):
            raise InvalidCredentials()
        expire = datetime.now(tz=timezone.utc) + timedelta(seconds=20)
        
        token = encode({'id': user.id, 'exp': expire}, os.getenv("JWT_PASS"), "HS256")

        result = {
            "token": token
        }

        return result