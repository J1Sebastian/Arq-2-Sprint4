from django.db import models

from medicamentos.models import Medicamento

class Procedimiento(models.Model):
    precio = models.IntegerField()
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    lectura = models.CharField(max_length=50)

    def __str__(self):
        return 'Procedimiento %s (%s)' % (str(self.nombre), str(self.codigo))
