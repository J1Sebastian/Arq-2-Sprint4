from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from models import Paciente

router = APIRouter()

# CRUD

# Create

@router.post("/create", response_description='Crear paciente', status_code=status.HTTP_201_CREATED)
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
    paciente = request.app.database["pacientes"].insert_one(paciente)
    return request.app.database["pacientes"].find_one(paciente.inserted_id)

@router.post("/", response_description='Crear paciente', status_code=status.HTTP_201_CREATED,response_model=Paciente)
def post_paciente_json(request: Request, paciente: Paciente = Body(...)):
    paciente = jsonable_encoder(paciente)
    new_paciente = request.app.database["pacientes"].insert_one(paciente)
    created_paciente = request.app.database["pacientes"].find_one(
        {"_id": new_paciente.inserted_id
    })
    return created_paciente


# Read

@router.get("/", response_description='Ver todos los pacientes', response_model=List[Paciente])
def get_pacientes(request: Request):
    pacientes = list(request.app.database["pacientes"].find())
    return pacientes

@router.get("/{id}", response_description='Ver paciente', response_model=Paciente)
def get_paciente(id: str, request: Request):
    paciente = request.app.database["pacientes"].find_one({"_id": id})
    if paciente is not None:
        return paciente
    raise HTTPException(status_code=404, detail=f"Paciente not found")


# Delete

@router.delete("/", response_description="Borrar todos los pacientes")
def delete_pacientes(request: Request):
    request.app.database["pacientes"].delete_many({})
    return {"message": "Pacientes borrados"}

@router.delete("/{id}", response_description="Borrar paciente")
def delete_paciente(id: str, request: Request):
    delete_result = request.app.database["pacientes"].delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return {"message": "Paciente borrado"}
    raise HTTPException(status_code=404, detail=f"Paciente {id} no encontrado")
