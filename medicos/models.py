from django.db import models

class Medico(models.Model):
    nombre: str = models.CharField(max_length=50)
    documento: str = models.CharField(max_length=50)
    especialidad: str = models.CharField(max_length=50)
    tarjeta_profesional: str = models.CharField(max_length=50)
    # telefono: str = models.CharField(max_length=50)
    # correo: str = models.CharField(max_length=50)
    # direccion: str = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Doctor(a) {self.nombre}, {self.especialidad} ({self.documento})"

# Create your models here.
