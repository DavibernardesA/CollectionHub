from http import HTTPStatus

from flask import Blueprint, request
from flask_restx import Resource
from pydantic_core import ValidationError

from adapters.resources.utils import pydantic_errors_to_request_error
from application.exceptions.collectionhub_exception import CollectionHubException
from application.users.create import Create
from application.users.detail import Detail
from application.users.login import Login
from domain.core.repositories.user_repository import UserRepository

user = Blueprint("users", __name__)


class UserResource(Resource):
    @classmethod
    @user.get("/users/<string:user_id>")
    def detail(user_id):
        try:
            user_detail = Detail(user_repository=UserRepository()).handler(
                user_id=user_id
            )
            return (user_detail, HTTPStatus.OK)
        except ValidationError as error:
            return (
                pydantic_errors_to_request_error(error.errors()),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        except CollectionHubException as error:
            return (
                error.to_dict(),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

    @classmethod
    @user.post("/users/auth/register")
    def create():
        try:
            user_create = Create(user_repository=UserRepository()).handler(
                body=request.get_json()
            )
            return (user_create, HTTPStatus.OK)
        except ValidationError as error:
            return (
                pydantic_errors_to_request_error(error.errors()),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        except CollectionHubException as error:
            return (
                error.to_dict(),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

    @classmethod
    @user.post("/users/auth/login")
    def login():
        try:
            user_login = Login(user_repository=UserRepository()).handler(
                body=request.get_json()
            )
            return (user_login, HTTPStatus.OK)
        except ValidationError as error:
            return (
                pydantic_errors_to_request_error(error.errors()),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
        except CollectionHubException as error:
            return (
                error.to_dict(),
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )