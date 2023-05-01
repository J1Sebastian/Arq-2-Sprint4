from .logic import ips_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ipss_view(request):
    if request.method == 'GET':
       id = request.GET.get('id')
       if id:
            ips_dto = vl.get_ips(id)
            data = serializers.serialize('json', [ips_dto, ])
            return HttpResponse(data, content_type='application/json')
       else:
            ipss_dto = vl.get_ipss()
            data = serializers.serialize('json', ipss_dto)
            return HttpResponse(data, content_type='application/json')
    if request.method == 'POST':
        ips_dto = vl.create_ips(json.loads(request.body))
        data = serializers.serialize('json', [ips_dto, ])
        return HttpResponse(data, content_type='application/json')
    
@csrf_exempt
def ips_view(request, id):
    if request.method == 'GET':
        ips_dto = vl.get_ips(id)
        data = serializers.serialize('json', [ips_dto, ])
        return HttpResponse(data, content_type='application/json')
    if request.method == 'PUT':
        ips_dto = vl.update_ips(id, json.loads(request.body))
        data = serializers.serialize('json', [ips_dto, ])
        return HttpResponse(data, content_type='application/json')
    if request.method == 'DELETE':
        ips_dto = vl.delete_ips(id)
        data = serializers.serialize('json', [ips_dto, ])
        return HttpResponse(data, content_type='application/json')