from eps.models import Eps
from pacientes.models import Paciente
from ..models import Afiliacion

def get_afiliaciones():
    afiliaciones = Afiliacion.objects.all()
    return afiliaciones

def get_afiliacion(id):
    afiliacion = Afiliacion.objects.get(id=id)
    return afiliacion

def create_afiliacion(afiliacion):
    paciente_pk = Paciente.objects.get(pk=afiliacion['paciente'])
    eps_pk = Eps.objects.get(pk=afiliacion['eps'])
    afiliacion = Afiliacion(paciente=paciente_pk, eps=eps_pk, regimen=afiliacion['regimen'])
    afiliacion.save()
    return afiliacion

def update_afiliacion(id, new_afiliacion):
    afiliacion = get_afiliacion(id)
    paciente_pk = Paciente.objects.get(pk=new_afiliacion['paciente'])
    eps_pk = Eps.objects.get(pk=new_afiliacion['eps'])
    afiliacion.regimen = new_afiliacion['regimen']
    afiliacion.save()
    return afiliacion

def delete_afiliacion(id):
    afiliacion = get_afiliacion(id)
    afiliacion.delete()
    return afiliacion