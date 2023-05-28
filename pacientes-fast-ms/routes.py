from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import PacienteModel

router = APIRouter()

@router.post("/", response_description='Crear paciente', status_code=status.HTTP_201_CREATED,response_model=PacienteModel)
def post_paciente(request: Request, paciente: PacienteModel = Body(...)):
    paciente = jsonable_encoder(paciente)
    new_paciente = request.app.database["pacientes"].insert_one(paciente)
    created_paciente = request.app.database["pacientes"].find_one(
        {"_id": new_paciente.inserted_id
    })
    return created_paciente

@router.post("/create", response_description='Crear paciente con parametros', status_code=status.HTTP_201_CREATED)
def create_paciente(nombre: str, documento: str, prioridad: str, fecha_nacimiento: str, peso: int, altura: int, tipo_sangre: str, request: Request):
    paciente = {
        "nombre": nombre,
        "documento": documento,
        "prioridad": prioridad,
        "fecha_nacimiento": fecha_nacimiento,
        "peso": peso,
        "altura": altura,
        "tipo_sangre": tipo_sangre
    }
    new_paciente = request.app.database["pacientes"].insert_one(paciente)
    return request.app.database["pacientes"].find_one({"_id": new_paciente.inserted_id})

@router.get("/{id}", response_description='Obtener paciente por id', response_model=PacienteModel)
def get_paciente(id: str, request: Request):
    paciente = request.app.database["pacientes"].find_one({"_id": id})
    if (paciente) is not None:
        return paciente
    raise HTTPException(status_code=404, detail=f"Paciente {id} no encontrado")

# Get all pacientes
@router.get("/", response_description='Obtener todos los pacientes', response_model=list[PacienteModel])
def get_pacientes(request: Request):
    pacientes = []
    for paciente in request.app.database["pacientes"].find():
        pacientes.append(paciente)
    return pacientes