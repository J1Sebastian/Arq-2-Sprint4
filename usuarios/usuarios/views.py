from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from . import logic as la
from django.http import HttpResponse
from django.core import serializers
import json

from django.http import JsonResponse

from .models import Usuario

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
    

def UsuarioList(request):
    queryset = Usuario.objects.all()
    context = list(queryset.values('id', 'nombre', 'documento', 'perfil'))
    return JsonResponse(context, safe=False)

def UsuarioCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        usuario = Usuario()
        usuario.nombre = data_json['nombre']
        usuario.documento = data_json['documento']
        usuario.perfil = data_json['perfil']
        usuario.save()
        return HttpResponse("successfully created usuario")
