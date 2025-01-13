from http import HTTPStatus

from flask import Blueprint, request
from flask_restx import Resource
from pydantic_core import ValidationError

from src.adapters.resources.utils import (
    get_query_params,
    pydantic_errors_to_request_error,
)
from src.application.exceptions.collectionhub_exception import CollectionHubException

from src.domain.core.repositories.item_repository import ItemRepository
from src.domain.core.repositories.collection_repository import CollectionRepository

from src.application.items.index import Index

item = Blueprint("items", __name__)

class ItemResource(Resource):
    @classmethod
    @item.get("/items/<collection_id>")
    def index(collection_id):
        try:
            items_index = Index(
                item_repository=ItemRepository(),
                collection_repository=CollectionRepository()
            ).handler(
                collection_id=collection_id, query_params=get_query_params(request.url)
            )
            return (items_index, HTTPStatus.OK)
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