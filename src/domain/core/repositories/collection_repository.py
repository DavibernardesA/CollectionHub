from domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface
) 
from src.db import DATABASE, get_cursor
from domain.core.models.collection import CollectionModel

class CollectionRepository(CollectionRepositoryInterface):
    def __init__(self):
        self.columns = [
            "id",
            "name",
            "item_count",
            "custom_attributes",
            "likes",
            "favorites",
            "followers",
            "status",
            "created_by",
            "created_at",
            "updated_at",
            "deleted_at",
            "errors"
        ]

    def find_all(self):
        cursor = get_cursor()
        cursor.execute(f"select * from {CollectionModel.Meta.db_name}")
        collection_data = cursor.fetchall()
        if collection_data:
            collections = [CollectionModel(**dict(zip(self.columns, collection))) for collection in collection_data]
            return collections
        return []