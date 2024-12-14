from bcrypt import gensalt, hashpw

from domain.core.models.user import UserModel
from domain.core.ports.repositories.user_repository_interface import (
    UserRepositoryInterface,
)
from utils import conn, cursor


class UserRepository(UserRepositoryInterface):
    def __init__(self):
        self.columns = [
            "id",
            "name",
            "email",
            "password",
            "account_type",
            "created_at",
            "updated_at",
        ]

    def insert_one(self, user: UserModel) -> UserModel:
        user_to_insert = user.model_dump()
        if "id" in user_to_insert:
            del user_to_insert["id"]

        pass_hash = hashpw(str.encode(user_to_insert["password"]), gensalt())

        result = cursor.execute(
            f"insert into {UserModel.Meta.db_name} (name, email, password, account_type, created_at, updated_at) "
            f"values (%s, %s, %s, %s, %s, %s) returning *",
            (
                user_to_insert["name"],
                user_to_insert["email"],
                pass_hash.decode(),
                user_to_insert["account_type"],
                user_to_insert["created_at"],
                user_to_insert["updated_at"],
            ),
        )
        conn.commit()
        inserted_user = result.fetchone()
        user_dict = dict(zip(self.columns, inserted_user))
        return UserModel(**user_dict)

    def find_by_email(self, email: str) -> UserModel | None:
        cursor.execute(
            f"select * from {UserModel.Meta.db_name} where email = %s", (email,)
        )
        user_data = cursor.fetchone()

        if user_data:
            user_dict = dict(zip(self.columns, user_data))
            return UserModel(**user_dict)

        return None

    def find_by_id(self, id: str) -> UserModel | None:
        cursor.execute(f"select * from {UserModel.Meta.db_name} where id = %s", (id,))
        user_data = cursor.fetchone()

        if user_data:
            user_dict = dict(zip(self.columns, user_data))
            return UserModel(**user_dict)

        return None

    def find_all(self) -> list[UserModel]:
        cursor.execute(f"select * from {UserModel.Meta.db_name}")
        user_data = cursor.fetchall()

        if user_data:
            users = [UserModel(**dict(zip(self.columns, row))) for row in user_data]
            return users

        return []

    def destroy_one(self, id: str) -> bool:
        user = self.find_by_id(id)
        if not user:
            return False
        
        cursor.execute(f"delete from {UserModel.Meta.db_name} where id = %s", (id,))
        
        if cursor.rowcount == 0:
            return False
        
        conn.commit()
        return True
    
    def update(self, user: UserModel, id: str) -> UserModel | None:
        user_to_insert = user.model_dump()
        if "id" in user_to_insert:
            del user_to_insert["id"]
        if "password" in user_to_insert:
                user_to_insert["password"] = hashpw(
                    str.encode(user_to_insert["password"]), gensalt()
                ).decode()    

        cursor.execute(
            f"update {UserModel.Meta.db_name} set name = %s, email = %s, password = %s, account_type = %s, updated_at = NOW() where id = %s returning *",
            (
            user_to_insert["name"],
            user_to_insert["email"],
            user_to_insert["password"],
            user_to_insert["account_type"],
            id,
            )
        )
        updated_user_data = cursor.fetchone()
        if not updated_user_data:
            return None
        
        conn.commit()

        updated_user_dict = dict(zip(self.columns, updated_user_data))
        updated_user_dict["id"] = id

        return UserModel(**updated_user_dict)