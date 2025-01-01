from src.application.exceptions.collectionhub_exception import CollectionHubException


class Unauthorized(CollectionHubException):
    def __init__(self):
        message = ("Unauthorized", "Nao autorizado")
        super().__init__(message, "unauthorized")
