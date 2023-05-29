from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'', views.UsuarioList, name='usuarioList'),
    url(r'^usuarioscreate/$', csrf_exempt(views.UsuarioCreate), name='usuarioCreate'),
]