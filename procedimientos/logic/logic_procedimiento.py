from ..models import Procedimiento

def get_procedimientos():
    queryset = Procedimiento.objects.all()
    return (queryset)


def get_procedimiento(procedimiento_pk):
    procedimiento = Procedimiento.objects.get(pk=procedimiento_pk)
    return procedimiento


def create_procedimiento(form):
    procedimiento = form.save()
    procedimiento.save()
    return ()


def update_procedimiento(procedimiento_pk, new_procedimiento):
    procedimiento = get_procedimiento(procedimiento_pk)
    procedimiento = new_procedimiento
    return procedimiento


def delete_procedimiento(procedimiento_pk):
    procedimiento = get_procedimiento(procedimiento_pk)
    procedimiento.delete()
    return ()
