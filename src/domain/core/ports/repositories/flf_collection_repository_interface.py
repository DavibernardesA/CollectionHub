from abc import ABC, abstractmethod

from src.domain.core.models.flf_collection import FLFCollection
from src.domain.core.models.value_objects.flf import FLFType


class FLFColllectionRepositoryInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def find_by_id_and_action(
        self, account_id: str, action: FLFType
    ) -> FLFCollection | None:
        pass

    @abstractmethod
    def create_action(
        self, account_id: str, action: FLFType, collection_id: str
    ) -> FLFCollection:
        pass

    @abstractmethod
    def delete(self, account_id: str, action: FLFType) -> None:
        pass
