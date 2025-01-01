from abc import ABC, abstractmethod

from src.domain.core.models.lock import LockModel


class LockRepositoryInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def lock(self, id: str) -> bool:
        pass

    @abstractmethod
    def unlock(self, id: str) -> bool:
        pass

    @abstractmethod
    def find_by_collection_id(self, collection_id: str) -> LockModel | None:
        pass
