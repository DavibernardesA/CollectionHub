from pydantic import Field
from domain.core.models.user import UserModel

class CreateUser(UserModel):
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=255)
    password: str
