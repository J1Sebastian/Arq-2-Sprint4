from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^pacientes/', views.PacienteList, name='pacienteList'),
    url(r'^pacientescreate/$', csrf_exempt(views.PacienteCreate), name='pacienteCreate'),
]
    