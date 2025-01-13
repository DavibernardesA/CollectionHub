from datetime import datetime, timezone
from uuid import UUID
from pydantic import BaseModel, Field, field_validator
from src.domain.core.models.collection import CollectionModel
from src.domain.core.models.user import UserModel

class ItemModel(BaseModel):
    id: UUID = Field(default_factory=UUID, description="Unique ID for each item")
    collection_id: UUID = Field(..., description="ID of the collection to which the item belongs")
    attributes: dict = Field(..., description="Attributes of the item, stored in JSON format")
    likes: int = Field(0, description="Number of likes")
    views: int = Field(0, description="Number of views")
    visibility: bool = Field(True, description="Visibility of the item")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Creation date")
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Last update date")

    @field_validator("id", mode="before")
    @classmethod
    def uuid_to_string(cls, v: str):
        if v is not None:
            return str(v)
        return v

    def model_dump(self):
        data = super().model_dump()
        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()
        return data
    
    @staticmethod
    def is_visible_to_user(user: UserModel, collection: CollectionModel):
        return user.is_admin or user.id == collection.id

    class Meta:
        db_name = "items"