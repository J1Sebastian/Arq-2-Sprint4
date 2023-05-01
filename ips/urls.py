from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ipss_view, name='ipss_view'),
    path('<int:id>', views.ips_view, name='ips_view'),
]