from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_paciente as lp
from django.http import HttpResponse
from django.core import serializers
import json

@csrf_exempt
def pacientes_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            paciente_dto = lp.get_paciente(id)
            paciente = serializers.serialize('json', [paciente_dto,])
            return HttpResponse(paciente, 'application/json')
        else:
            pacientes_dto = lp.get_pacientes()
            pacientes = serializers.serialize('json', pacientes_dto)
            return HttpResponse(pacientes, 'application/json')

    if request.method == 'POST':
        paciente_dto = lp.create_paciente(json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    
@csrf_exempt
def paciente_view(request, pk):
    if request.method == 'GET':
        paciente_dto = lp.get_paciente(pk)
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')

    if request.method == 'PUT':
        paciente_dto = lp.update_paciente(pk, json.loads(request.body))
        paciente = serializers.serialize('json', [paciente_dto,])
        return HttpResponse(paciente, 'application/json')
    
    if request.method == 'DELETE':
        lp.delete_paciente(pk)
        return HttpResponse(status=204)

    