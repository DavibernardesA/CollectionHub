from domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from domain.core.models.dtos.create_user import UserModel 
from flask import request
from domain.core.models.value_objects.user_type import UserType
from application.exceptions.unauthorized_exception import Unauthorized
from application.exceptions.users.user_already_exists_exception import UserAlreadyExists
from application.exceptions.users.user_must_exists_exception import UserMustExists

class Update:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository
        
    def handler(self, user_id: str, body: dict) -> dict:
        dto = UserModel(**body)

        own_account = request.user.id == user_id
        is_admin = request.user.account_type == UserType.ADMIN

        # Verifica se o usuário tem permissão para atualizar
        if not own_account and not is_admin:
            raise Unauthorized()

        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise UserMustExists()

        # Apenas ADMIN pode promover usuários a ADMIN
        if dto.account_type == UserType.ADMIN and not is_admin:
            dto.account_type = UserType.USER

        # Administradores nao podem se rabaixar
        if user.account_type == UserType.ADMIN and dto.account_type == UserType.USER:
            raise Unauthorized()

        user_with_same_email = self.user_repository.find_by_email(dto.email)
        if user_with_same_email and user_with_same_email.id != user_id:
            raise UserAlreadyExists()

        self.user_repository.update(dto, user_id)

        return {}
