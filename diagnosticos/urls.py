from django.urls import path

from . import views

urlpatterns = [
    path('', views.diagnosticos_view, name='diagnosticos_view'),
    path('<int:pk>', views.diagnostico_view, name='diagnostico_view'),
]
    