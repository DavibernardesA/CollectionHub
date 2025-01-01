from typing import List
from pydantic import BaseModel, Field, FieldValidationInfo, field_validator

class CustomAttribute(BaseModel):
    name: str = Field(..., description="Nome do atributo personalizado")
    type: str = Field(..., description="Tipo do atributo personalizado (bool, int, float, str, date)")

    @field_validator("type")
    @classmethod
    def validate_type(cls, value: str, _: FieldValidationInfo) -> str:
        allowed_types = {"bool", "int", "float", "str", "date"}
        if value not in allowed_types:
            raise ValueError(f"Invalid type: {value}. Allowed types are: {', '.join(allowed_types)}")
        return value

class CustomAttributesDTO(BaseModel):
    attributes: List[CustomAttribute]