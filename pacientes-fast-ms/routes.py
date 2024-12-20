from datetime import date
import uuid
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Union
from models import Paciente, PacientePrioritario
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

# CRUD

# Create

@router.post("/create", response_description='Crear paciente', status_code=status.HTTP_201_CREATED,response_model=Union[Paciente,PacientePrioritario])
def create_paciente(nombre: str, documento: str, prioridad: str, fecha_nacimiento: str, peso: int, altura: int, tipo_sangre: str, request: Request):
    altura_m = altura / 100
    bmi = round(peso / (altura_m * altura_m), 2)
    print(bmi)
    obeso = False
    if bmi < 18.5:
        tipo_peso = "BAJO PESO"
    elif bmi >= 18.5 and bmi < 25:
        tipo_peso = "NORMAL"
    elif bmi >= 25 and bmi < 30:
        tipo_peso = "SOBREPESO"
    elif bmi >= 30 and bmi < 35:
        obeso = True
        tipo_peso = "OBESIDAD TIPO I"
    elif bmi >= 35 and bmi < 40:
        obeso = True
        tipo_peso = "OBESIDAD TIPO II"
    else:
        obeso = True
        tipo_peso = "OBESIDAD TIPO III"
    print(tipo_peso)

    paciente = {
        "_id": str(uuid.uuid4()),
        "nombre": nombre,
        "documento": documento,
        "prioridad": prioridad,
        "fecha_nacimiento": fecha_nacimiento,
        "peso": peso,
        "altura": altura,
        "tipo_sangre": tipo_sangre
    }
    if obeso:
        paciente["BMI"] = bmi
        paciente["tipo_peso"] = tipo_peso
        bd = "pacientes_prioritarios"
    else:
        bd = "pacientes"

    print("Anormal" if obeso else "Normal")

    paciente = request.app.database[bd].insert_one(paciente)
    created_paciente = request.app.database[bd].find_one(
        {"_id": paciente.inserted_id
    })
    return created_paciente

@router.post("/", response_description='Crear paciente', status_code=status.HTTP_201_CREATED,response_model=Paciente)
def post_paciente_json(request: Request, paciente: Paciente = Body(...)):
    paciente = jsonable_encoder(paciente)
    new_paciente = request.app.database["pacientes"].insert_one(paciente)
    created_paciente = request.app.database["pacientes"].find_one(
        {"_id": new_paciente.inserted_id
    })
    return created_paciente

# Post priority patient

@router.post("/prioritario", response_description='Crear paciente prioritario', status_code=status.HTTP_201_CREATED, response_model=PacientePrioritario)
def post_paciente_prioritario_json(request: Request, paciente: PacientePrioritario = Body(...)):
    paciente = jsonable_encoder(paciente)
    new_paciente = request.app.database["pacientes_prioritarios"].insert_one(paciente)
    created_paciente = request.app.database["pacientes_prioritarios"].find_one(
        {"_id": new_paciente.inserted_id
    })
    return created_paciente

# Read

@router.get("/", response_description='Ver todos los pacientes', response_model=List[Paciente])
def get_pacientes(request: Request):
    pacientes = list(request.app.database["pacientes"].find())
    return pacientes

@router.get("/home", response_description='Ver todos los pacientes', response_model=List[Paciente])
def get_pacientes(request: Request):
    pacientes = list(request.app.database["pacientes"].find().limit(10))
    return templates.TemplateResponse("pacientes.html", {"request": request, "pacientes": pacientes})

# Get prioritary patients
@router.get("/prioritario", response_description='Ver todos los pacientes prioritarios', response_model=List[PacientePrioritario])
def get_pacientes(request: Request):
    pacientes = list(request.app.database["pacientes_prioritarios"].find())
    return pacientes

# Get prioritary patients older than 18
@router.get("/prioritario18", response_description='Ver todos los pacientes prioritarios', response_model=List[PacientePrioritario])
def get_pacientes(request: Request):
    #Get today's date as string in format YYYY-MM-DD
    today = date.today()
    today = today.replace(year=today.year - 18)
    today = today.strftime("%Y-%m-%d")
    pacientes = list(request.app.database["pacientes_prioritarios"].find({"fecha_nacimiento": {"$lte": today}}).limit(100))
    return pacientes


# Get prioritary patients older than 18
@router.get("/consulta", response_description='Ver todos los pacientes prioritarios', response_model=List[PacientePrioritario])
def get_pacientes(request: Request):
    #Get today's date as string in format YYYY-MM-DD
    today = date.today()
    today = today.replace(year=today.year - 18)
    today = today.strftime("%Y-%m-%d")
    pacientes = list(request.app.database["pacientes_prioritarios"].find({"fecha_nacimiento": {"$lte": today}}).limit(10))
    return templates.TemplateResponse("pacientes_prioritarios18.html", {"request": request, "pacientes": pacientes})


# @router.get("/{id}", response_description='Ver paciente', response_model=Paciente)
# def get_paciente(id: str, request: Request):
#     paciente = request.app.database["pacientes"].find_one({"_id": id})
#     if paciente is not None:
#         return paciente
#     raise HTTPException(status_code=404, detail=f"Paciente not found")


# Delete

@router.delete("/", response_description="Borrar todos los pacientes")
def delete_pacientes(request: Request):
    request.app.database["pacientes"].delete_many({})
    return {"message": "Pacientes borrados"}


@router.delete("/prioritario", response_description="Borrar todos los pacientes prioritarios")
def delete_pacientes_prioritarios(request: Request):
    request.app.database["pacientes_prioritarios"].delete_many({})
    return {"message": "Pacientes prioritarios borrados"}


# @router.delete("/{id}", response_description="Borrar paciente")
# def delete_paciente(id: str, request: Request):
#     delete_result = request.app.database["pacientes"].delete_one({"_id": id})
#     if delete_result.deleted_count == 1:
#         return {"message": "Paciente borrado"}
#     raise HTTPException(status_code=404, detail=f"Paciente {id} no encontrado")


# Fill database
@router.post("/filldb", response_description="Llenar la base de datos")
def fill_database(n_pacientes: int, n_prioritarios: int, request: Request):
    paciente_pri = {
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
    paciente = {
        "nombre": "Nicolás Carvajal",
        "documento": "1267835678",
        "prioridad": "BAJA",
        "fecha_nacimiento": "2000-10-19",
        "peso": 40,
        "altura": 130,
        "tipo_sangre": "B+",
    }
    for i in range(n_pacientes):
        paciente["_id"] = str(uuid.uuid4())
        paciente = jsonable_encoder(paciente)
        request.app.database["pacientes"].insert_one(paciente)
    for i in range(n_prioritarios):
        paciente_pri["_id"] = str(uuid.uuid4())
        paciente = jsonable_encoder(paciente_pri)
        request.app.database["pacientes_prioritarios"].insert_one(paciente)
    return {"message": f"Se llenó la base de datos con {n_pacientes} pacientes y {n_prioritarios} pacientes prioritarios"}