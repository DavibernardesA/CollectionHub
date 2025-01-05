from pydantic import BaseModel, Field, ValidationInfo, field_validator

from src.domain.core.models.value_objects.flf import FLFType

class FLFItem(BaseModel):
    item_id: str = Field(..., description="Item ID")
    action: FLFType
    account_id: str = Field(..., description="User ID")

    @field_validator("account_id", "item_id", mode="before")
    @classmethod
    def uuid_to_string(cls, v: str, info: ValidationInfo):
        if v is not None:
            return str(v)
        return v

    def model_dump(self):
        data = super().model_dump()
        return data

    class Meta:
        db_name = "flf_items"
