
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.epss_view, name='epss_view'),
    path('<int:id>', views.eps_view, name='eps_view'),
]