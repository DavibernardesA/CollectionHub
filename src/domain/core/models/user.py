from pydantic import BaseModel, Field, field_validator, ValidationInfo
from datetime import datetime, timezone
import hashlib
import bcrypt

class UserModel(BaseModel):
    id: str | None = Field(None, max_length=255, description="User ID")
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=255)
    password: str
    account_type: str
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

    def password_check(self, pwd_candidate: str) -> bool:
        if not self.password:
            return False
        
        hash = hashlib.sha1(pwd_candidate.encode("utf-8")).hexdigest().encode("utf-8")

        pwd_hash = self.password.encode("utf-8")
        return bcrypt.checkpw(hash, pwd_hash)

    class Meta:
        db_name = "users"
