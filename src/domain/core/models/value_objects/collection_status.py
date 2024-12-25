from enum import Enum

class CollectionStatus(str, Enum):
    DRAFT = "draft"
    INCOMPLETE = "incomplete"
    ACTIVE = "active"
    DELETED = "deleted"

    def __str__(self):
        return str(self.value)