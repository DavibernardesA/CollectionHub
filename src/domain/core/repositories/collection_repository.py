import json

from src.db import DATABASE, get_cursor
from src.domain.core.models.collection import CollectionModel
from src.domain.core.models.value_objects.collection_status import CollectionStatus
from src.domain.core.ports.repositories.collection_repository_interface import (
    CollectionRepositoryInterface,
)


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
    
    def find_all(self, status: CollectionStatus = None) -> list[CollectionModel]:
        cursor = get_cursor()

        query = f"select * from {CollectionModel.Meta.db_name}"

        if status and status == CollectionStatus.DELETED:
            query += " where status = %s"
            cursor.execute(query, (status,))
        elif status and status != CollectionStatus.DELETED:
            query += " where status = %s"
            cursor.execute(query, (status,))
        
        if not status:
            query += " where status != %s"
            cursor.execute(query, (CollectionStatus.DELETED,))

        collection_data = cursor.fetchall()
        if collection_data:
            return [
                CollectionModel(**dict(zip(self.columns, collection)))
                for collection in collection_data
            ]
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

    def update_custom_attributes(
        self, id: str, attributes: list, status: CollectionStatus
    ) -> CollectionModel | None:
        cursor = get_cursor()

        json_attributes = json.dumps(attributes)

        cursor.execute(
            f"""
            UPDATE {CollectionModel.Meta.db_name}
            SET custom_attributes = custom_attributes || %s::jsonb,
                status = %s,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = %s
            RETURNING *
            """,
            (json_attributes, status.value, id),
        )

        updated_collection_data = cursor.fetchone()
        if not updated_collection_data:
            return None

        DATABASE.commit()

        updated_collection_dict = dict(zip(self.columns, updated_collection_data))
        return CollectionModel(**updated_collection_dict)

    def delete(
        self, collection_id: str, permanently: bool = False, status: CollectionStatus = None
    ) -> None:
        cursor = get_cursor()

        if permanently:
            query = f"DELETE FROM {CollectionModel.Meta.db_name} WHERE id = %s"
            params = (collection_id,)

        else:
            query = f"UPDATE {CollectionModel.Meta.db_name} SET status = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s"
            params = (status, collection_id)

        cursor.execute(
            query,
            params,
        )
        DATABASE.commit()
        return
