from abc import ABC, abstractmethod

from src.domain.core.models.item import ItemModel

class ItemRepositoryInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def find_items_by_collection(self, collection_id: str) -> list[ItemModel]:
        pass

    @abstractmethod
    def find_by_id(self, item_id: str) -> ItemModel | None:
        pass

    @abstractmethod
    def insert_one(self, body: ItemModel) -> ItemModel:
        pass

    @abstractmethod
    def update(self, body: ItemModel) -> None:
        pass

    @abstractmethod
    def delete(self, item_id: str) -> None:
        pass