from src.domain.core.ports.repositories.flf_collection_repository_interface import FLFColllectionRepositoryInterface
from src.db import DATABASE, get_cursor
from src.domain.core.models.flf_collection import FLFCollection

class FLFCollectionRepository(FLFColllectionRepositoryInterface):
    def __init__(self):
        self.columns = [
            "account_id",
            "action",
            "collection_id"
        ]

    def find_by_id_and_action(self, account_id, action):
        cursor = get_cursor()

        query = f"select * from {FLFCollection.Meta.db_name} where account_id = %s and action = %s"

        params = (account_id, action)

        cursor.execute(
            query,
            params
        )

        action_data = cursor.fetchone()
        if not action_data:
            return None
        
        action_dict = dict(zip(self.columns, action_data))

        return FLFCollection(**action_dict)
    
    def create_action(self, account_id, action, collection_id):
        cursor = get_cursor()

        query = f"insert into {FLFCollection.Meta.db_name} (account_id, action, collection_id) values (%s, %s, %s) returning *"

        params = (account_id, action, collection_id)

        cursor.execute(
            query,
            params,
        )
        DATABASE.commit()
        created_action = cursor.fetchone()
        action_dict = dict(zip(self.columns, created_action))

        return FLFCollection(**action_dict)
    
    def delete(self, account_id, action):
        cursor = get_cursor()

        query = f"delete from {FLFCollection.Meta.db_name} where account_id = %s and action = %s"

        params = (account_id, action)

        cursor.execute(
            query,
            params,
        )
        DATABASE.commit()
        return