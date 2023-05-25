from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from historiasclinicas.forms import HistoriaClinicaForm
from registrador_logs.logIdDev import encryptId
from .logic import logic_historia_clinica as hl
from django.http import HttpResponse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
import json
from forms import HistoriaClinicaForm
from django.contrib.auth.decorators import login_required
from autenticador.auth0backend import getRole, getUserId

import requests

@csrf_exempt
def historia_clinica_list(request):
    historiasclinicas = hl.get_historiasclinicas()
    context = {
        'historia_clinica_list': historiasclinicas
    }
    return render(request, 'historiasclinicas/historiasclinicas.html', context)

@csrf_exempt
def historiasclinicas_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            historia_clinica_dto = hl.get_historia_clinica(id)
            historia_clinica = serializers.serialize('json', [historia_clinica_dto,])
            return HttpResponse(historia_clinica, 'application/json')
        else:
            historiasclinicas_dto = hl.get_historiasclinicas()
            historiasclinicas = serializers.serialize('json', historiasclinicas_dto)
            return HttpResponse(historiasclinicas, 'application/json')

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
    historiasclinicas = hl.get_historiasclinicas()
    historiasclinicas = historiasclinicas.order_by('-id')[:10]
    context = {
        'historia_clinica_list': historiasclinicas
    }

    return render(request, 'historiasclinicas/historiasclinicas.html', context)

@login_required
def historia_clinica_edit_view(request, id):
    role = getRole(request)
    if role == "medico":
        if request.method == 'PUT':
            form = HistoriaClinicaForm(request.PUT)
            if form.is_valid():
                historia_clinica = hl.update_historia_clinica(id, form)
                historia_clinica.save()
                messages.success(request, 'Historia clinica editada correctamente')
                return HttpResponseRedirect(reverse('home'))
            else:
                print(form.errors)
        else:
            form = HistoriaClinicaForm()

        context = {
            'form': form
        }
        return render(request, 'historiasclinicas/historia_clinica_edit.html', context)
    else:
        return HttpResponse("No tiene permisos para editar historias clinicas")
    
@login_required
def historia_clinica_create_view(request):
    role = getRole(request)
    if role == "medico":
        if request.method == 'POST':
            form = HistoriaClinicaForm(request.POST)
            if form.is_valid():
                historia_clinica = form.save()
                historia_clinica.save()
                encryptId(getUserId(request), getRole(request), historia_clinica.fecha_creacion, historia_clinica.codigo)
                messages.success(request, 'Historia clinica creada correctamente')
                return HttpResponseRedirect(reverse('home'))
            else:
                print(form.errors)
        else:
            form = HistoriaClinicaForm()

        context = {
            'form': form
        }
        return render(request, 'historiasclinicas/historia_clinica_create.html', context)
    else:
        return HttpResponse("No tiene permisos para crear historias clinicas")