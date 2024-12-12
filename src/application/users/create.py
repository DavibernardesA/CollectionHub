from domain.core.ports.repositories.user_repository_interface import UserRepositoryInterface
from application.exceptions.users.user_already_exists_exception import UserAlreadyExists
from domain.core.models.dtos.create_user import CreateUser

class Create:
    def __init__(
            self,
            user_repository: UserRepositoryInterface
            ) -> None:
        self.user_repository = user_repository

    def handler(self, body: dict) -> dict:
        body["account_type"] = "user"

        dto = CreateUser(**body)

        user = self.user_repository.find_by_email(dto.email)

        if user:
            raise UserAlreadyExists()
        
        created_user = self.user_repository.insert_one(dto)

        return created_user.model_dump()