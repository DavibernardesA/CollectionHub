from http import HTTPStatus

from flask import Blueprint, request
from flask_restx import Resource
from pydantic_core import ValidationError

from src.adapters.resources.utils import get_query_params, pydantic_errors_to_request_error
from src.application.exceptions.collectionhub_exception import CollectionHubException
from src.domain.core.repositories.collection_repository import CollectionRepository
from src.domain.core.repositories.user_repository import UserRepository
from src.application.collections.create import Create
from src.application.collections.detail import Detail
from src.application.collections.index import Index

collection = Blueprint("collection", __name__)


class CollectionResource(Resource):
    @classmethod
    @collection.get("/collections")
    def index():
        try:
            collection_index = Index(
                collection_repository=CollectionRepository()
            ).handler(query_params=get_query_params(request.url))
            return (collection_index, HTTPStatus.OK)
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
    @collection.get("/collections/<string:collection_id>")
    def detail(collection_id):
        try:
            collection_index = Detail(
                collection_repository=CollectionRepository()
            ).handler(collection_id=collection_id)
            return (collection_index, HTTPStatus.OK)
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
    @collection.post("/collections/create")
    def create():
        try:
            collection_create = Create(
                collection_repository=CollectionRepository(),
                user_repository=UserRepository(),
            ).handler(body=request.json)
            return (collection_create, HTTPStatus.CREATED)
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
