from django.urls import path

from . import views

urlpatterns = [
    path('', views.consultas_view, name='consultas_view'),
    path('<int:pk>', views.consulta_view, name='consulta_view'),
]
    