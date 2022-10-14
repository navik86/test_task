from pydantic import BaseModel, Field


class Validator(BaseModel):
    article: int = Field(alias="id")
    name: str
    brand: str