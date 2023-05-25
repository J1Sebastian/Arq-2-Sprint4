# from medicamentos.logic.logic_medicamentos import get_medicamento
# from diagnosticos.logic.logic_diagnostico import get_diagnostico
# from consultas.logic.logic_consulta import get_consulta
# from pacientes.logic.logic_paciente import get_paciente
# from procedimientos.logic.logic_procedimiento import get_procedimiento, get_procedimientos
from ..models import HistoriaClinica

def get_historiasclinicas():
    queryset = HistoriaClinica.objects.all()
    return (queryset)


def get_historia_clinica(historia_clinica_pk):
    historia_clinica = HistoriaClinica.objects.get(pk=historia_clinica_pk)
    return historia_clinica

def replace_historia_clinica(historia_clinica_pk, new_historia_clinica):
    HistoriaClinica.objects.update_or_create(pk=historia_clinica_pk, defaults=new_historia_clinica)
    return new_historia_clinica


def create_historia_clinica(form):
    historia_clinica = form.save()
    historia_clinica.save()
    return ()

def create_historia_clinica_json(historia_clinica_json: dict):
    historia_clinica = HistoriaClinica(
        fecha_creacion = historia_clinica_json['fecha_creacion'],
        antecedentes = historia_clinica_json['antecedentes'],
        alergias = historia_clinica_json['alergias'],
        # medicamentos = get_medicamento(historia_clinica_json['medicamentos']),
        # procedimientos = get_procedimiento(historia_clinica_json['procedimientos']),
        # diagnosticos = get_diagnostico(historia_clinica_json['diagnosticos']),
        # consultas = get_consulta(historia_clinica_json['consultas']),
        # paciente = get_paciente(historia_clinica_json['paciente']),
    )
    historia_clinica.save()
    return historia_clinica


def update_historia_clinica_json(pk, historia_clinica_json: dict):
    historia_clinica = get_historia_clinica(pk)
    # historia_clinica_json['procedimientos'] = get_procedimiento(historia_clinica_json['procedimientos'])
    # historia_clinica_json['medicamentos'] = get_medicamento(historia_clinica_json['medicamentos'])
    # historia_clinica_json['diagnosticos'] = get_diagnostico(historia_clinica_json['diagnosticos'])
    # historia_clinica_json['consultas'] = get_consulta(historia_clinica_json['consultas'])
    # historia_clinica_json['paciente'] = get_paciente(historia_clinica_json['paciente'])
    replace_historia_clinica(pk, historia_clinica_json)
    historia_clinica.save()
    return historia_clinica
    

def update_historia_clinica(historia_clinica_pk, new_historia_clinica):
    historia_clinica = get_historia_clinica(historia_clinica_pk)
    historia_clinica.fecha_creacion = new_historia_clinica.fecha_creacion
    historia_clinica.antecedentes = new_historia_clinica.antecedentes
    historia_clinica.alergias = new_historia_clinica.alergias
    historia_clinica.medicamentos = new_historia_clinica.medicamentos
    historia_clinica.procedimientos = new_historia_clinica.procedimientos
    historia_clinica.diagnosticos = new_historia_clinica.diagnosticos
    historia_clinica.consultas = new_historia_clinica.consultas
    historia_clinica.paciente = new_historia_clinica.paciente
    historia_clinica.save()
    return historia_clinica



