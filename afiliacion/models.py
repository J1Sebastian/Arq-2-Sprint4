from django.db import models

subsidiario: str = "SUBSIDIARIO"
contributivo_cotizante: str = "CONTRIBUTIVO_COTIZANTE"
contributivo_beneficiario: str = "CONTRIBUTIVO_BENEFICIARIO"

class Afiliacion(models.Model):
    paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.CASCADE)
    eps = models.ForeignKey('eps.Eps', on_delete=models.CASCADE)
    regimen = models.CharField(max_length=50) # SUBSIDIARIO, CONTRIBUTIVO_COTIZANTE, CONTRIBUTIVO_BENEFICIARIO

    def __str__(self) -> str:
        return f"EPS: {self.eps}, Paciente: {self.paciente}"
