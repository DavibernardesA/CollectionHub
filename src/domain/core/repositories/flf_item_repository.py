from src.domain.core.ports.repositories.flf_item_repository_interface import FLFItemRepositoryInterface
from src.db import DATABASE, get_cursor
from src.domain.core.models.flf_item import FLFItem

class FLFCollectionRepository(FLFItemRepositoryInterface):
    def __init__(self):
        self.columns = [
            "account_id",
            "action",
            "item_id"
        ]

    def find_by_id_and_action(self, account_id, action):
        cursor = get_cursor()

        query = f"select * from {FLFItem.Meta.db_name} where account_id = %s and action = %s"

        params = (account_id, action)

        cursor.execute(
            query,
            params
        )

        action_data = cursor.fetchone()
        if not action_data:
            return None
        
        action_dict = dict(zip(self.columns, action_data))

        return FLFItem(**action_dict)
    
    def delete(self, account_id, action):
        cursor = get_cursor()

        query = f"delete from {FLFItem.Meta.db_name} where account_id = %s and action = %s "

        params = (account_id, action)

        cursor.execute(
            query,
            params,
        )
        DATABASE.commit()
        return