from django.db import models

class Medicamento(models.Model):    
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    nombre = models.CharField(max_length=50)
    dosis = models.IntegerField()
    frecuencia = models.IntegerField()
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return '%s, %s' % (str(self.nombre), str(self.dosis))
    
