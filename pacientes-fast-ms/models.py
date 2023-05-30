from typing import Optional
import uuid;
from pydantic import BaseModel, Field

alta : str = "ALTA"
media : str = "MEDIA"
baja : str = "BAJA"

class Paciente(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
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
                "documento": "1021981819",
                "prioridad": "BAJA",
                "fecha_nacimiento": "2003-11-12",
                "peso": 70,
                "altura": 172,
                "tipo_sangre": "O+"
            }
        }

class PacientePrioritario(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    nombre: str = Field(...)
    documento: str = Field(...)
    prioridad: str = Field(...)
    fecha_nacimiento: str = Field(...)
    peso: int = Field(...)
    altura: int = Field(...)
    tipo_sangre: str = Field(...)
    BMI: float = Field(...)
    tipo_peso: str = Field(...)
    
    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "nombre": "Armando Pérez",
                "documento": "52672861",
                "prioridad": "ALTA",
                "fecha_nacimiento": "1998-11-15",
                "peso": 100,
                "altura": 179,
                "tipo_sangre": "O+",
                "BMI": 30.86,
                "tipo_peso": "OBESIDAD TIPO I"
            }
        }