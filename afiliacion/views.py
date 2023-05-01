from .logic import afiliacion_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def afiliaciones_view(request):
    if request.method == 'GET':
       id = request.GET.get('id')
       if id:
            afiliacion_dto = vl.get_afiliacion(id)
            data = serializers.serialize('json', [afiliacion_dto, ])
            return HttpResponse(data, content_type='application/json', status=200)
       else:
            afiliaciones_dto = vl.get_afiliaciones()
            data = serializers.serialize('json', afiliaciones_dto)
            return HttpResponse(data, content_type='application/json', status=200)
    if request.method == 'POST':
        afiliacion_dto = vl.create_afiliacion(json.loads(request.body))
        data = serializers.serialize('json', [afiliacion_dto, ])
        return HttpResponse(data, content_type='application/json', status=201)
    

@csrf_exempt
def afiliacion_view(request, id):
    if request.method == 'GET':
        afiliacion_dto = vl.get_afiliacion(id)
        data = serializers.serialize('json', [afiliacion_dto, ])
        return HttpResponse(data, content_type='application/json', status=200)
    if request.method == 'PUT':
        afiliacion_dto = vl.update_afiliacion(id, json.loads(request.body))
        data = serializers.serialize('json', [afiliacion_dto, ])
        return HttpResponse(data, content_type='application/json', status=200)
    if request.method == 'DELETE':
        afiliacion_dto = vl.delete_afiliacion(id)
        data = serializers.serialize('json', [afiliacion_dto, ])
        return HttpResponse(data, content_type='application/json', status=200)