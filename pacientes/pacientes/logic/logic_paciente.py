from ..models import Paciente

def get_pacientes():
    queryset = Paciente.objects.all()
    return (queryset)

def get_paciente(paciente_pk):
    paciente = Paciente.objects.get(pk=paciente_pk)
    return paciente

def create_paciente(form):
    paciente = form.save()
    paciente.save()
    return ()

def update_paciente(paciente_pk, new_paciente):
    paciente = get_paciente(paciente_pk)
    paciente.nombres = new_paciente.nombres
    paciente.apellidos = new_paciente.apellidos
    paciente.fecha_nacimiento = new_paciente.fecha_nacimiento
    paciente.genero = new_paciente.genero
    paciente.tipo_sangre = new_paciente.tipo_sangre
    paciente.save()
    return paciente