from pydantic import Field

from src.domain.core.models.user import UserModel


class CreateUser(UserModel):
    password_admin: str | None = Field(None, max_length=255, description="admin password")
