from abc import ABC, abstractmethod

from src.domain.core.models.user import UserModel


class UserRepositoryInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def insert_one(self, body: UserModel) -> UserModel:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> UserModel | None:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> UserModel | None:
        pass

    @abstractmethod
    def find_all(
        self,
    ) -> list[UserModel]:
        pass

    @abstractmethod
    def destroy_one(self, id: str) -> bool:
        pass

    @abstractmethod
    def update(self, body: UserModel, id: str) -> UserModel | None:
        pass
