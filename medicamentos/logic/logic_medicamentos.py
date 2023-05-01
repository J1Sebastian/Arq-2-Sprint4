from ..models import Medicamento

def get_medicamentos():
    queryset = Medicamento.objects.all()
    return (queryset)


def get_medicamento(medicamento_pk):
    medicamento = Medicamento.objects.get(pk=medicamento_pk)
    return medicamento


def create_medicamento(form):
    medicamento = form.save()
    medicamento.save()
    return ()


def update_medicamento(medicamento_pk, new_medicamento):
    medicamento = get_medicamento(medicamento_pk)
    medicamento = new_medicamento
    return medicamento


def delete_medicamento(medicamento_pk):
    medicamento = get_medicamento(medicamento_pk)
    medicamento.delete()
    return ()




