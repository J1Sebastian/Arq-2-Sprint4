from django.views.decorators.csrf import csrf_exempt
from .logic import logic_diagnostico as dg
from django.http import HttpResponse
from django.core import serializers
import json
    
@csrf_exempt
def diagnosticos_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            diagnostico_dto = dg.get_diagnostico(id)
            diagnostico = serializers.serialize('json', [diagnostico_dto,])
            return HttpResponse(diagnostico, 'application/json')
        else:
            diagnosticos_dto = dg.get_diagnosticos()
            diagnosticos = serializers.serialize('json', diagnosticos_dto)
            return HttpResponse(diagnosticos, 'application/json')

    if request.method == 'POST':
        diagnostico_dto = dg.create_diagnostico(json.loads(request.body))
        diagnostico = serializers.serialize('json', [diagnostico_dto,])
        return HttpResponse(diagnostico, 'application/json')
    
@csrf_exempt
def diagnostico_view(request, pk):
    if request.method == 'GET':
        diagnostico_dto = dg.get_diagnostico(pk)
        diagnostico = serializers.serialize('json', [diagnostico_dto,])
        return HttpResponse(diagnostico, 'application/json')

    if request.method == 'PUT':
        diagnostico_dto = dg.update_diagnostico(pk, json.loads(request.body))
        diagnostico = serializers.serialize('json', [diagnostico_dto,])
        return HttpResponse(diagnostico, 'application/json')
    
    if request.method == 'DELETE':
        dg.delete_diagnostico(pk)
        return HttpResponse(status=204)
    