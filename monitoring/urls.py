"""monitoring URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('eps/', include('eps.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('ips/', include('ips.urls')),
    path('historias_clinicas/', include('historias_clinicas.urls')),
    path('afiliacion/', include('afiliacion.urls')),
    path('medicamentos/', include('medicamentos.urls')),
    path('procedimientos/', include('procedimientos.urls')),
    path('diagnosticos/', include('diagnosticos.urls')),
    path('consultas/', include('consultas.urls')),
    path('medicos/', include('medicos.urls')),
    path('health-check/', views.health_check),
]
