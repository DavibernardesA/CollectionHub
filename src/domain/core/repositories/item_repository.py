from src.db import DATABASE, get_cursor

from src.domain.core.ports.repositories.item_repository_interface import ItemRepositoryInterface
from src.domain.core.models.item import ItemModel


class ItemRepository(ItemRepositoryInterface):
    def __init__(self):
        super().__init__()
        self.columns = [
            "id",
            "collection_id",
            "attributes",
            "likes",
            "views",
            "visibility",
            "created_at",
            "updated_at",
        ]

    def find_items_by_collection(self, collection_id: str) -> list[ItemModel]:
        cursor = get_cursor()

        query = f"select * from {ItemModel.Meta.db_name} where collection_id = %s"

        params = (collection_id,)

        cursor.execute(
            query,
            params
        )

        items_data = cursor.fetchall()

        if items_data:
            return [
                ItemModel(**dict(zip(self.columns, item)))
                for item in items_data
            ]
        
        return []
    
    def find_by_id(self, item_id: str) -> ItemModel | None:
        pass

    def insert_one(self, body: ItemModel) -> ItemModel:
        pass

    def update(self, body: ItemModel) -> None:
        pass

    def delete(self, item_id: str) -> None:
        pass