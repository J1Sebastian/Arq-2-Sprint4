from django.urls import path

from . import views

urlpatterns = [
    path('', views.procedimientos_view, name='procedimientos_view'),
    path('<int:pk>', views.procedimiento_view, name='procedimiento_view'),
]
    