from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.historias_clinicas_view, name='historias_clinicas_view'),
    path('<int:pk>', views.historia_clinica_view, name='historia_clinica_view'),
    path('historia_clinica_create/', csrf_exempt(views.historia_clinica_create), name='historia_clinica_create'),
    path('historia_clinica_put/<int:pk>/', csrf_exempt(views.historia_clinica_put), name='historia_clinica_put'),
]
    