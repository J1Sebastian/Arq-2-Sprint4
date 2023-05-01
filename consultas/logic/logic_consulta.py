from ..models import Consulta

def get_consultas():
    queryset = Consulta.objects.all()
    return (queryset)

def get_consulta(consulta_pk):
    consulta = Consulta.objects.get(pk=consulta_pk)
    return consulta

def create_consulta(form):
    consulta = form.save()
    consulta.save()
    return ()

def update_consulta(consulta_pk, new_consulta):
    consulta = get_consulta(consulta_pk)
    consulta.fecha = new_consulta.fecha
    consulta.precio = new_consulta.precio
    consulta.paciente = new_consulta.paciente
    consulta.medico = new_consulta.medico
    consulta.save()
    return consulta

def delete_consulta(consulta_pk):
    consulta = get_consulta(consulta_pk)
    consulta.delete()
    return ()