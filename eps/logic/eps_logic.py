
from ..models import Eps


def get_epss():
    epss = Eps.objects.all()
    return epss

def get_eps(id):
    eps = Eps.objects.get(id)
    return eps

def create_eps(eps):
    eps = Eps(nombre=eps['nombre'], nit=eps['nit'])
    eps.save()
    return eps

def update_eps(id, new_eps):
    eps = get_eps(id)
    eps.nombre = new_eps['nombre']
    eps.nit = new_eps['nit']
    eps.save()
    return eps

def delete_eps(id):
    eps = get_eps(id)
    eps.delete()
    return eps