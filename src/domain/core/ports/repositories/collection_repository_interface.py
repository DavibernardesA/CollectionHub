from abc import ABC, abstractmethod

from src.domain.core.models.collection import CollectionModel
from src.domain.core.models.value_objects.collection_status import CollectionStatus
from src.domain.core.models.value_objects.flf import FLFType


class CollectionRepositoryInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def find_all(
        self,
        status: CollectionStatus | None = None,
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

    @abstractmethod
    def update_custom_attributes(self, id: str, body: dict) -> CollectionModel | None:
        pass

    @abstractmethod
    def recive_action(
        self, action: FLFType, collection_id: str, negative: bool
    ) -> CollectionModel | None:
        pass

    @abstractmethod
    def delete(
        self,
        collection_id: str,
        permanently: bool = False,
        status: CollectionStatus = None,
    ) -> None:
        pass
