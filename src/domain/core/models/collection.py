from datetime import datetime, timezone
from pydantic import BaseModel, Field, ValidationInfo, constr, field_validator
from domain.core.models.value_objects.collection_status import CollectionStatus


class CollectionModel(BaseModel):
    id: constr(max_length=255) = Field(None, max_length=255, description="Collection ID")
    name: constr(max_length=255) = Field(..., max_length=100)
    item_count: int = Field(0, description="Number of items in the collection")
    custom_attributes: dict = Field({}, description="Custom attributes for the collection")
    likes: int = Field(0, description="Number of likes in the collection")
    favorites: int = Field(0, description="Number of favorites in the collection")
    followers: int = Field(0, description="Number of followers in the collection")
    status: CollectionStatus
    created_by: str = Field(..., description="User ID that created the collection")
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="created_at",
        title="Criado em",
    )
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="updated_at",
        title="Modificado em",
    )
    deleted_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        description="updated_at",
        title="Deletado em",
    )
    errors: list = Field([], description="List of errors in the collection")

    @field_validator("id", mode="before")
    @classmethod
    def uuid_to_string(cls, v: str, info: ValidationInfo):
        if v is not None:
            return str(v)
        return v

    def model_dump(self, exclude_password: bool = False):
        data = super().model_dump()

        data["created_at"] = data["created_at"].isoformat()
        data["updated_at"] = data["updated_at"].isoformat()

        if exclude_password:
            data.pop("password", None)
        return data

    class Meta:
        db_name = "collections"
