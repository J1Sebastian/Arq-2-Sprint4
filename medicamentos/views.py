from django.views.decorators.csrf import csrf_exempt
from .logic import logic_medicamentos as md
from django.http import HttpResponse
from django.core import serializers
import json
    
@csrf_exempt
def medicamentos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            medicamento_dto = md.get_medicamento(id)
            medicamento = serializers.serialize('json', [medicamento_dto,])
            return HttpResponse(medicamento, 'application/json')
        else:
            medicamentos_dto = md.get_medicamentos()
            medicamentos = serializers.serialize('json', medicamentos_dto)
            return HttpResponse(medicamentos, 'application/json')

    if request.method == 'POST':
        medicamento_dto = md.create_medicamento(json.loads(request.body))
        medicamento = serializers.serialize('json', [medicamento_dto,])
        return HttpResponse(medicamento, 'application/json')

@csrf_exempt
def medicamento_view(request, pk):
    if request.method == 'GET':
        medicamento_dto = md.get_medicamento(pk)
        medicamento = serializers.serialize('json', [medicamento_dto,])
        return HttpResponse(medicamento, 'application/json')

    if request.method == 'PUT':
        medicamento_dto = md.update_medicamento(pk, json.loads(request.body))
        medicamento = serializers.serialize('json', [medicamento_dto,])
        return HttpResponse(medicamento, 'application/json')
    
    if request.method == 'DELETE':
        md.delete_medicamento(pk)
        return HttpResponse(status=204)
    


    