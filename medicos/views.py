from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_medico as lm
from django.http import HttpResponse
from django.core import serializers
import json

@csrf_exempt
def medicos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            medico_dto = lm.get_medico(id)
            medico = serializers.serialize('json', [medico_dto,])
            return HttpResponse(medico, 'application/json')
        else:
            medicos_dto = lm.get_medicos()
            medicos = serializers.serialize('json', medicos_dto)
            return HttpResponse(medicos, 'application/json')

    if request.method == 'POST':
        medico_dto = lm.create_medico(json.loads(request.body))
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')
    
@csrf_exempt
def medico_view(request, pk):
    if request.method == 'GET':
        medico_dto = lm.get_medico(pk)
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')

    if request.method == 'PUT':
        medico_dto = lm.update_medico(pk, json.loads(request.body))
        medico = serializers.serialize('json', [medico_dto,])
        return HttpResponse(medico, 'application/json')
    
    if request.method == 'DELETE':
        lm.delete_medico(pk)
        return HttpResponse(status=204)
