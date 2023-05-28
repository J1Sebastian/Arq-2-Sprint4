from typing import Optional
import uuid;
from pydantic import BaseModel, Field


class ListModel(BaseModel):
    id:str = Field(default_factory=uuid.uuid4, alias="_id")
    nombre: str
    documento: str

class ListUpdateModel(BaseModel):
    nombre: Optional[str]
    documento: Optional[str]
