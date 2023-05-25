from django.db import models

enfermero : str = "ENFERMERO"
medico : str = "MEDICO"
admin_sistema : str = "ADMINISTRADOR DEL SISTEMA"
personal_admin: str = "PERSONAL ADMINISTRATIVO"

class Usuario(models.Model):
    nombre: str = models.CharField(max_length=50)
    documento: str = models.CharField(max_length=50)
    perfil: str = models.CharField(max_length=50) 

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Documento: {self.documento}, Perfil: {self.perfil}"

# Create your models here.
