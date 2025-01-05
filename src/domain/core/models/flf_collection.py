from pydantic import BaseModel, Field, ValidationInfo, field_validator

from src.domain.core.models.value_objects.flf import FLFType


class FLFCollection(BaseModel):
    collection_id: str = Field(..., description="Collection ID")
    action: FLFType
    account_id: str = Field(..., description="User ID")

    @field_validator("account_id", "collection_id", mode="before")
    @classmethod
    def uuid_to_string(cls, v: str, info: ValidationInfo):
        if v is not None:
            return str(v)
        return v

    def model_dump(self):
        data = super().model_dump()
        return data

    class Meta:
        db_name = "flf_collections"
