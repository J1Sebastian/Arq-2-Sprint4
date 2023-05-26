from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from . import logic as lp
from django.http import HttpResponse
from django.core import serializers
from django.http import JsonResponse

import json

from .models import Paciente

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


def PacienteList(request):
    #queryset = Paciente.objects.all()
    #context = list(queryset.values('id', 'nombre', 'documento', 'prioridad', 'fecha_nacimiento', 'peso', 'altura', 'tipo_sangre'))

    queryset = Paciente.objects.all()
    pacientes = queryset.order_by('-id')[:10]
    context = {
        'pacientes_list': pacientes
    }
    return render(request, 'pacientes.html', context)


def PacienteCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        paciente = Paciente()
        paciente.nombre = data_json["nombre"]
        paciente.documento = data_json["documento"]
        paciente.prioridad = data_json["prioridad"]
        paciente.fecha_nacimiento = data_json["fecha_nacimiento"]
        paciente.peso = data_json["peso"]
        paciente.altura = data_json["altura"]
        paciente.tipo_sangre = data_json["tipo_sangre"]
        paciente.save()
        return HttpResponse("successfully created paciente")