from django.db import models

publica: str = "PUBLICA"
privada: str = "PRIVADA"
mixta: str = "MIXTA"

centro: str = "CENTRO"
clinica: str = "CLINICA"
otro: str = "OTRO"

b : str = "B"
c1 : str = "C1"
c2 : str = "C2"
d1 : str = "D1"
d2 : str = "D2"
d3 : str = "D3"

class Ips(models.Model):
    nombre: str = models.CharField(max_length=50)
    centro: str = models.CharField(max_length=50) # HOSPITAL, CLINICA, OTRO
    financiacion: str = models.CharField(max_length=50) # PUBLICA, PRIVADA, MIXTA
    tamano: str = models.CharField(max_length=50) # B, C1, C2, D1, D2, D3
    epss: models.ManyToManyField('eps.Eps')

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Financiacion: {self.financiacion}"
