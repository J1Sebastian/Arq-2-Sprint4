from django.db import models

class Diagnostico(models.Model):
    nombre = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return 'Diagnóstico: %s' % (self.nombre)
    