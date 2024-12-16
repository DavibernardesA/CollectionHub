import os

from flask import request
from jwt import ExpiredSignatureError, decode, DecodeError, InvalidTokenError
from domain.core.repositories.user_repository import UserRepository
from src.settings import PUBLIC_ROUTES
from domain.core.models.user import UserModel

def exec() -> UserModel | bool:
    if request.path in PUBLIC_ROUTES:
        return True

    bearer_token = request.headers.get("Authorization")

    if not bearer_token or not bearer_token.startswith("Bearer "):
        return False

    token = bearer_token.split(" ")[1]

    try:
        user_data = decode(token, os.getenv("JWT_PASS"), algorithms=["HS256"])
        user = UserRepository().find_by_id(user_data["id"])

        if not user:
            return False

        return UserModel(**user.model_dump())
    except ExpiredSignatureError:
        return False
    except (DecodeError, InvalidTokenError):
        return False
    except Exception as e:
        return False