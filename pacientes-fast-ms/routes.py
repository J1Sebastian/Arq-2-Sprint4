from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import PacienteModel

router = APIRouter()

@router.post("/", response_description='Crear paciente', status_code=status.HTTP_201_CREATED,response_model=PacienteModel)
def create_paciente(request: Request, paciente: PacienteModel = Body(...)):
    paciente = jsonable_encoder(paciente)
    new_paciente = request.app.database["pacientes"].insert_one(paciente)
    created_paciente = request.app.database["pacientes"].find_one(
        {"_id": new_paciente.inserted_id
    })
    return created_paciente