from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from historias_clinicas.forms import HistoriaClinicaForm
from .logic import logic_historia_clinica as hl
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
import json

@csrf_exempt
def historia_clinica_list(request):
    historias_clinicas = hl.get_historias_clinicas()
    context = {
        'historia_clinica_list': historias_clinicas
    }
    return render(request, 'historias_clinicas/historias_clinicas.html', context)

@csrf_exempt
def historias_clinicas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            historia_clinica_dto = hl.get_historia_clinica(id)
            historia_clinica = serializers.serialize('json', [historia_clinica_dto,])
            return HttpResponse(historia_clinica, 'application/json')
        else:
            historias_clinicas_dto = hl.get_historias_clinicas()
            historias_clinicas = serializers.serialize('json', historias_clinicas_dto)
            return HttpResponse(historias_clinicas, 'application/json')

    if request.method == 'POST':
        historia_clinica_dto = hl.create_historia_clinica(json.loads(request.body))
        historia_clinica = serializers.serialize('json', [historia_clinica_dto,])
        return HttpResponse(historia_clinica, 'application/json')

@csrf_exempt
def historia_clinica_view(request, pk):
    if request.method == 'GET':
        historia_clinica_dto = hl.get_historia_clinica(pk)
        historia_clinica = serializers.serialize('json', [historia_clinica_dto,])
        return HttpResponse(historia_clinica, 'application/json')

    if request.method == 'PUT':
        historia_clinica_dto = hl.update_historia_clinica(pk, json.loads(request.body))
        historia_clinica = serializers.serialize('json', [historia_clinica_dto,])
        return HttpResponse(historia_clinica, 'application/json')
    
    if request.method == 'DELETE':
        hl.delete_historia_clinica(pk)
        return HttpResponse(status=204)

@csrf_exempt
def historia_clinica_create(request):
    if request.method == 'POST':
        historia_clinica_dto = hl.create_historia_clinica_json(json.loads(request.body))
        historia_clinica = serializers.serialize('json', [historia_clinica_dto,])
        return HttpResponse(historia_clinica, 'application/json')
    
@csrf_exempt
def historia_clinica_put(request, pk):
    if request.method == 'PUT':
        historia_clinica_dto = hl.update_historia_clinica_json(pk, json.loads(request.body))
        historia_clinica = serializers.serialize('json', [historia_clinica_dto,])
        return HttpResponse(historia_clinica, 'application/json')

@csrf_exempt
def crear_historia_clinica_view(request):
    if request.method == 'POST':
        historia_clinica_dto = hl.create_historia_clinica(json.loads(request.body))
        historia_clinica = serializers.serialize('json', [historia_clinica_dto,])
        return HttpResponse(historia_clinica, 'application/json')
@csrf_exempt
def home(request):
    historias_clinicas = hl.get_historias_clinicas()
    historias_clinicas = historias_clinicas.order_by('-id')[:10]
    context = {
        'historia_clinica_list': historias_clinicas
    }

    return render(request, 'historias_clinicas/historias_clinicas.html', context)

def historia_clinica_edit_view(request, id):
    historia_clinica = hl.get_historia_clinica(id)
    context = {
        'historia_clinica': historia_clinica
    }
    return render(request, 'historias_clinicas/historia_clinica_edit.html', context)