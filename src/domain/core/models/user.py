from datetime import datetime, timezone
from bcrypt import checkpw

from pydantic import BaseModel, Field, ValidationInfo, field_validator, constr

from domain.core.models.value_objects.user_type import UserType


class UserModel(BaseModel):
    id: constr(max_length=255) = Field(None, max_length=255, description="User ID")
    name: constr(max_length=255) = Field(..., max_length=100)
    email: constr(max_length=255) = Field(..., max_length=255)
    password: constr(max_length=255) = Field(..., max_length=255)
    account_type: UserType
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

    def password_check(self, dto_password: str, compared_password: str) -> bool:
        right_password = checkpw(str.encode(dto_password), str.encode(compared_password))
        return right_password

    class Meta:
        db_name = "users"
