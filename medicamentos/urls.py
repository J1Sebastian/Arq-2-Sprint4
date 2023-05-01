from django.urls import path

from . import views

urlpatterns = [
    path('', views.medicamentos_view, name='medicamentos_view'),
    path('<int:pk>', views.medicamento_view, name='medicamento_view'),
]
    