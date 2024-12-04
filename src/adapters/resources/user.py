from http import HTTPStatus

from flask import Blueprint
from flask_restx import Resource

user = Blueprint("users", __name__)


class UserResource(Resource):
    @classmethod
    @user.get("/users")
    def index():
        return {"user": {"user": "John Doe"}}, HTTPStatus.OK
