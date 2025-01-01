from pydantic import BaseModel, Field, ValidationInfo, constr, field_validator


class LockModel(BaseModel):
    id: constr(max_length=255) = Field(None, max_length=255, description="Lock ID")
    collection_id: constr(max_length=255) = Field(
        ..., max_length=255, description="Collection ID"
    )

    @field_validator("id", "collection_id", mode="before")
    @classmethod
    def uuid_to_string(cls, v: str, info: ValidationInfo):
        if v is not None:
            return str(v)
        return v

    def model_dump(self):
        data = super().model_dump()
        return data

    class Meta:
        db_name = "locks"
