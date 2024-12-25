from abc import ABC, abstractmethod


class CollectionRepositoryInterface(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def find_all(
        self,
    ) -> list:
        pass