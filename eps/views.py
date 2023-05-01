from .logic import eps_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def epss_view(request):
    if request.method == 'GET':
       id = request.GET.get('id')
       if id:
            eps_dto = vl.get_eps(id)
            data = serializers.serialize('json', [eps_dto, ])
            return HttpResponse(data, content_type='application/json')
       else:
            epss_dto = vl.get_epss()
            data = serializers.serialize('json', epss_dto)
            return HttpResponse(data, content_type='application/json')
    if request.method == 'POST':
        eps_dto = vl.create_eps(json.loads(request.body))
        data = serializers.serialize('json', [eps_dto, ])
        return HttpResponse(data, content_type='application/json')
    
@csrf_exempt
def eps_view(request, id):
    if request.method == 'GET':
        eps_dto = vl.get_eps(id)
        data = serializers.serialize('json', [eps_dto, ])
        return HttpResponse(data, content_type='application/json')
    if request.method == 'PUT':
        eps_dto = vl.update_eps(id, json.loads(request.body))
        data = serializers.serialize('json', [eps_dto, ])
        return HttpResponse(data, content_type='application/json')
    if request.method == 'DELETE':
        eps_dto = vl.delete_eps(id)
        data = serializers.serialize('json', [eps_dto, ])
        return HttpResponse(data, content_type='application/json')