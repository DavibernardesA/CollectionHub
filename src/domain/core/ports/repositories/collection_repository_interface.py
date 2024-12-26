from abc import ABC, abstractmethod

from domain.core.models.collection import CollectionModel


class CollectionRepositoryInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def find_all(
        self,
    ) -> list:
        pass

    @abstractmethod
    def find_by_id(self, id: str) -> CollectionModel | None:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> CollectionModel | None:
        pass

    @abstractmethod
    def insert_one(self, body: CollectionModel) -> CollectionModel | None:
        pass
