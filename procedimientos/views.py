from django.views.decorators.csrf import csrf_exempt
from .logic import logic_procedimiento as pl
from django.http import HttpResponse
from django.core import serializers
import json
    
@csrf_exempt
def procedimientos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            procedimiento_dto = pl.get_procedimiento(id)
            procedimiento = serializers.serialize('json', [procedimiento_dto,])
            return HttpResponse(procedimiento, 'application/json')
        else:
            procedimientos_dto = pl.get_procedimientos()
            procedimientos = serializers.serialize('json', procedimientos_dto)
            return HttpResponse(procedimientos, 'application/json')

    if request.method == 'POST':
        procedimiento_dto = pl.create_procedimiento(json.loads(request.body))
        procedimiento = serializers.serialize('json', [procedimiento_dto,])
        return HttpResponse(procedimiento, 'application/json')
    
@csrf_exempt
def procedimiento_view(request, pk):
    if request.method == 'GET':
        procedimiento_dto = pl.get_procedimiento(pk)
        procedimiento = serializers.serialize('json', [procedimiento_dto,])
        return HttpResponse(procedimiento, 'application/json')

    if request.method == 'PUT':
        procedimiento_dto = pl.update_procedimiento(pk, json.loads(request.body))
        procedimiento = serializers.serialize('json', [procedimiento_dto,])
        return HttpResponse(procedimiento, 'application/json')
    
    if request.method == 'DELETE':
        pl.delete_procedimiento(pk)
        return HttpResponse(status=204)
    