from http import HTTPStatus

from flask import Blueprint, request
from flask_restx import Resource
from pydantic_core import ValidationError

from adapters.resources.utils import get_query_params, pydantic_errors_to_request_error
from application.exceptions.collectionhub_exception import CollectionHubException
from application.users.create import Create
from application.users.delete import Destroy
from application.users.detail import Detail
from application.users.index import Index
from application.users.login import Login
from application.users.update import Update
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

    @classmethod
    @user.get("/users")
    def index():
        try:
            user_index = Index(user_repository=UserRepository()).handler(
                query_params=get_query_params(request.url)
            )
            return (user_index, HTTPStatus.OK)
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
    @user.put("/users/<string:user_id>")
    def update(user_id):
        try:
            user_update = Update(user_repository=UserRepository()).handler(
                user_id=user_id, body=request.get_json()
            )
            return (user_update, HTTPStatus.OK)
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
    @user.delete("/users/<string:user_id>")
    def delete(user_id):
        try:
            user_delete = Destroy(user_repository=UserRepository()).handler(
                user_id=user_id
            )
            return (user_delete, HTTPStatus.NO_CONTENT)
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
