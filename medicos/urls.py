from django.urls import path

from . import views

urlpatterns = [
    path('', views.medicos_view, name='medicos_view'),
    path('<int:pk>', views.medico_view, name='medico_view'),
]