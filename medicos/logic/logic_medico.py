from ..models import Medico

def get_medicos():
    queryset = Medico.objects.all()
    return (queryset)

def get_medico(medico_pk):
    medico = Medico.objects.get(pk=medico_pk)
    return medico

def create_medico(form):
    medico = form.save()
    medico.save()
    return ()

def update_medico(medico_pk, new_medico):
    medico = get_medico(medico_pk)
    medico.nombres = new_medico.nombres
    medico.apellidos = new_medico.apellidos
    medico.fecha_nacimiento = new_medico.fecha_nacimiento
    medico.genero = new_medico.genero
    medico.tipo_sangre = new_medico.tipo_sangre
    medico.save()
    return medico