from abc import ABC, abstractmethod

from src.domain.core.models.flf_item import FLFItem
from src.domain.core.models.value_objects.flf import FLFType


class FLFItemRepositoryInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def find_by_id_and_action(self, account_id: str, action: FLFType) -> FLFItem | None:
        pass

    @abstractmethod
    def create_action(self, account_id: str, action: FLFType, item_id: str) -> FLFItem:
        pass

    @abstractmethod
    def delete(self, account_id: str, action: FLFType) -> None:
        pass
