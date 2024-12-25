from http import HTTPStatus
from flask import Blueprint, request
from flask_restx import Resource
from src.application.collections.index import Index
from domain.core.repositories.collection_repository import CollectionRepository
from adapters.resources.utils import get_query_params, pydantic_errors_to_request_error
from pydantic_core import ValidationError
from application.exceptions.collectionhub_exception import CollectionHubException


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