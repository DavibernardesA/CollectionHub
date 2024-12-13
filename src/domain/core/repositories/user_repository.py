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
