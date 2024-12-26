from domain.core.models.collection import CollectionModel
from domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)
from src.db import DATABASE, get_cursor


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
            "errors",
        ]

    def find_all(self) -> list[CollectionModel]:
        cursor = get_cursor()
        cursor.execute(f"select * from {CollectionModel.Meta.db_name}")
        collection_data = cursor.fetchall()
        if collection_data:
            collections = [
                CollectionModel(**dict(zip(self.columns, collection)))
                for collection in collection_data
            ]
            return collections
        return []

    def find_by_id(self, id: str) -> CollectionModel | None:
        cursor = get_cursor()
        cursor.execute(
            f"select * from {CollectionModel.Meta.db_name} where id = %s", (id,)
        )
        collection_data = cursor.fetchone()

        if collection_data:
            collection_dict = dict(zip(self.columns, collection_data))
            return CollectionModel(**collection_dict)
        return None

    def find_by_name(self, name) -> CollectionModel | None:
        cursor = get_cursor()
        cursor.execute(
            f"select * from {CollectionModel.Meta.db_name} where name = %s", (name,)
        )
        collection_data = cursor.fetchone()

        if collection_data:
            collection_dict = dict(zip(self.columns, collection_data))
            return CollectionModel(**collection_dict)
        return None

    def insert_one(self, body: CollectionModel) -> CollectionModel:
        collection_to_insert = body.model_dump()
        if "id" in collection_to_insert:
            del collection_to_insert["id"]

        cursor = get_cursor()

        cursor.execute(
            f"""
            INSERT INTO {CollectionModel.Meta.db_name}
            (name, item_count, likes, favorites, followers, status, created_by, created_at, updated_at, deleted_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING *
            """,
            (
                collection_to_insert["name"],
                collection_to_insert["item_count"],
                collection_to_insert["likes"],
                collection_to_insert["favorites"],
                collection_to_insert["followers"],
                collection_to_insert["status"],
                collection_to_insert["created_by"],
                collection_to_insert["created_at"],
                collection_to_insert["updated_at"],
                collection_to_insert["deleted_at"],
            ),
        )
        DATABASE.commit()

        inserted_collection = cursor.fetchone()
        user_dict = dict(zip(self.columns, inserted_collection))
        return CollectionModel(**user_dict)
