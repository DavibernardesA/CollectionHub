from src.application.exceptions.collectionhub_exception import CollectionHubException


class InvalidCredentials(CollectionHubException):
    def __init__(self):
        message = ("Invalid credentials", "Credenciais invalidas")
        super().__init__(message, "invalid_credential")
