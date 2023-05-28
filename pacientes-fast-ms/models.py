from typing import Optional
import uuid;
from pydantic import BaseModel, Field

alta : str = "ALTA"
media : str = "MEDIA"
baja : str = "BAJA"

class Paciente(BaseModel):
    id: int = Field(default_factory=uuid.uuid4, alias="_id")
    nombre: str = Field(...)
    documento: str = Field(...)
    prioridad: str = Field(...)
    fecha_nacimiento: str = Field(...)
    peso: int = Field(...)
    altura: int = Field(...)
    tipo_sangre: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "nombre": "Emilo Rozo",
                "documento": "1783981819",
                "prioridad": "ALTA",
                "fecha_nacimiento": "2020-01-01",
                "peso": 80,
                "altura": 180,
                "tipo_sangre": "O+"
            }
        }
