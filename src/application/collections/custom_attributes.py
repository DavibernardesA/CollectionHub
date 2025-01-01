from src.domain.core.ports.repositories.collection_repository_interface import CollectionRepositoryInterface

class CustomAtributes:
    def __init__(self, collection_repository: CollectionRepositoryInterface):
        self.collection_repository = collection_repository

    def handler(self):
        pass