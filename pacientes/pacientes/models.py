from django.db import models

alta : str = "ALTA"
media : str = "MEDIA"
baja : str = "BAJA"

class Paciente(models.Model):

    nombre: str = models.CharField(max_length=50)
    documento: str = models.CharField(max_length=50)
    prioridad: str = models.CharField(max_length=50) # ALTA, MEDIA, BAJA
    fecha_nacimiento: str = models.DateField()
    peso: int = models.IntegerField()
    altura: int = models.IntegerField()
    tipo_sangre: str = models.CharField(max_length=50)


    def __str__(self) -> str:
        return f"Paciente {self.nombre} | ID: {self.documento}"
    
    
