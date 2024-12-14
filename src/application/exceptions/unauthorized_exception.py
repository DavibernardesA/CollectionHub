from application.exceptions.collectionhub_exception import CollectionHubException


class Unauthorized(CollectionHubException):
    def __init__(self, msg: tuple = ("Unauthorized", "Nao autorizado")):
        message = msg
        super().__init__(message, "unauthorized")
