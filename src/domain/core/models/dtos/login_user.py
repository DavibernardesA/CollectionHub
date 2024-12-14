from pydantic import BaseModel, Field


class LoginUser(BaseModel):
    email: str = Field(..., max_length=255)
    password: str | None = Field(None, max_length=255)
