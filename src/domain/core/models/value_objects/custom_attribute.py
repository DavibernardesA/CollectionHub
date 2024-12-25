from pydantic import BaseModel, Field, constr

class CustomAttribute(BaseModel):
    name: constr(max_length=255) = Field(..., description="Name of the attribute")
    type: constr(max_length=50) = Field(..., description="Type of the attribute")
