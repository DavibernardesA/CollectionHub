from src.adapters.middlewares import get_user_by_request
from src.application.exceptions.unauthorized_exception import Unauthorized
from src.application.exceptions.users.user_already_exists_exception import (
    UserAlreadyExists,
)
from src.application.exceptions.users.user_must_exists_exception import UserMustExists
from src.domain.core.models.dtos.create_user import UserModel
from src.domain.core.models.value_objects.user_type import UserType
from src.domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)


class Update:
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def handler(self, user_id: str, body: dict) -> dict:
        dto = UserModel(**body)

        jwt_data = get_user_by_request.exec()

        if not jwt_data.has_permission(user_id):
            raise Unauthorized()

        user = self.user_repository.find_by_id(user_id)
        if not user:
            raise UserMustExists()

        if not jwt_data.can_promote_to_admin(dto.account_type):
            dto.account_type = UserType.USER

        # Administradores nao podem se rabaixar
        if user.is_admin() and not dto.is_admin():
            raise Unauthorized()

        user_with_same_email = self.user_repository.find_by_email(dto.email)
        if user_with_same_email and user_with_same_email.id != user_id:
            raise UserAlreadyExists()

        self.user_repository.update(dto, user_id)

        return {}
