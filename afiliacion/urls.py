
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.afiliaciones_view, name='afiliaciones_view'),
    path('<int:pk>', views.afiliacion_view, name='afiliacion_view'),
]