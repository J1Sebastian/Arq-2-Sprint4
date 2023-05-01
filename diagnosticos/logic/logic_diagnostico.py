from ..models import Diagnostico

def get_diagnosticos():
    queryset = Diagnostico.objects.all()
    return (queryset)

def get_diagnostico(diagnostico_pk):
    diagnostico = Diagnostico.objects.get(pk=diagnostico_pk)
    return diagnostico

def create_diagnostico(form):
    diagnostico = form.save()
    diagnostico.save()
    return ()

def update_diagnostico(diagnostico_pk, new_diagnostico):
    diagnostico = get_diagnostico(diagnostico_pk)
    diagnostico = new_diagnostico
    return diagnostico

def delete_diagnostico(diagnostico_pk):
    diagnostico = get_diagnostico(diagnostico_pk)
    diagnostico.delete()
    return ()