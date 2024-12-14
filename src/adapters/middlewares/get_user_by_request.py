import os

from flask import make_response, request
from jwt import ExpiredSignatureError, decode

from domain.core.repositories.user_repository import UserRepository


def exec():
    if request.path in ["/users/auth/register", "/users/auth/login"]:
        return
    bearer_token = request.headers.get("authorization")

    if not bearer_token:
        return make_response({"error": "Unauthorized."}, 401)

    token = bearer_token.replace("Bearer ", "")

    try:
        user_data = decode(token, os.getenv("JWT_PASS"), algorithms=["HS256"])
        user = UserRepository().find_by_id(user_data["id"])

        if not user:
            return make_response({"error": "Unathorized"}, 401)

        request.user = user
        return
    except ExpiredSignatureError:
        return make_response(
            {
                "id": "expired_token",
                "message": "Expired token",
                "meta": {"errors": {"user": "Expired token"}},
            },
            401,
        )
