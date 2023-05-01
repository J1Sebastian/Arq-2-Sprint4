from django.db import models
from pacientes.models import Paciente

publica: str = "PUBLICA"
privada: str = "PRIVADA"
mixta: str = "MIXTA"

class Eps(models.Model):
    nombre: str = models.CharField(max_length=50)
    financiacion: str = models.CharField(max_length=50) # PUBLICA, PRIVADA, MIXTA
    afiliados = models.ManyToManyField(Paciente, through='afiliacion.Afiliacion')
    ipss = models.ManyToManyField('ips.Ips')


    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Financiacion: {self.financiacion}"

