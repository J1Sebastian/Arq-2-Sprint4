from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .logic import logic_usuario as la
from django.http import HttpResponse
from django.core import serializers
import json

@csrf_exempt
def usuarios_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            usuario_dto = la.get_usuario(id)
            usuario = serializers.serialize('json', [usuario_dto,])
            return HttpResponse(usuario, 'application/json')
        else:
            usuarios_dto = la.get_usuarios()
            usuarios = serializers.serialize('json', usuarios_dto)
            return HttpResponse(usuarios, 'application/json')

    if request.method == 'POST':
        usuario_dto = la.create_usuario(json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')
    
@csrf_exempt
def usuario_view(request, pk):
    if request.method == 'GET':
        usuario_dto = la.get_usuario(pk)
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')

    if request.method == 'PUT':
        usuario_dto = la.update_usuario(pk, json.loads(request.body))
        usuario = serializers.serialize('json', [usuario_dto,])
        return HttpResponse(usuario, 'application/json')
    
    if request.method == 'DELETE':
        la.delete_usuario(pk)
        return HttpResponse(status=204)
