from django.views.decorators.csrf import csrf_exempt
from .logic import logic_consulta as ct
from django.http import HttpResponse
from django.core import serializers
import json

@csrf_exempt
def consultas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            consulta_dto = ct.get_consulta(id)
            consulta = serializers.serialize('json', [consulta_dto,])
            return HttpResponse(consulta, 'application/json')
        else:
            consultas_dto = ct.get_consultas()
            consultas = serializers.serialize('json', consultas_dto)
            return HttpResponse(consultas, 'application/json')

    if request.method == 'POST':
        consulta_dto = ct.create_consulta(json.loads(request.body))
        consulta = serializers.serialize('json', [consulta_dto,])
        return HttpResponse(consulta, 'application/json')
    
@csrf_exempt
def consulta_view(request, pk):
    if request.method == 'GET':
        consulta_dto = ct.get_consulta(pk)
        consulta = serializers.serialize('json', [consulta_dto,])
        return HttpResponse(consulta, 'application/json')

    if request.method == 'PUT':
        consulta_dto = ct.update_consulta(pk, json.loads(request.body))
        consulta = serializers.serialize('json', [consulta_dto,])
        return HttpResponse(consulta, 'application/json')
    
    if request.method == 'DELETE':
        ct.delete_consulta(pk)
        return HttpResponse(status=204)

    