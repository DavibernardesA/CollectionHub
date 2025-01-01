from src.db import DATABASE, get_cursor
from src.domain.core.models.lock import LockModel


class LockRepository:
    def __init__(self):
        self.columns = ["id", "collection_id"]

    def lock(self, collection_id: str) -> None:
        cursor = get_cursor()
        cursor.execute(
            f"insert into {LockModel.Meta.db_name} (collection_id) values (%s) on conflict do nothing",
            (collection_id,),
        )
        DATABASE.commit()

    def unlock(self, collection_id: str) -> None:
        cursor = get_cursor()
        cursor.execute(
            f"delete from {LockModel.Meta.db_name} where collection_id = %s",
            (collection_id,),
        )
        DATABASE.commit()

    def find_by_collection_id(self, collection_id: str) -> LockModel | None:
        cursor = get_cursor()
        cursor.execute(
            f"select * from {LockModel.Meta.db_name} where collection_id = %s",
            (collection_id,),
        )
        lock_data = cursor.fetchone()
        lock_dict = dict(zip(self.columns, lock_data))
        return LockModel(**lock_dict)
