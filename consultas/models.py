from django.db import models

class Consulta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    precio = models.IntegerField()
    paciente = models.ForeignKey('pacientes.Paciente', on_delete=models.CASCADE, null=True)
    medico = models.ForeignKey('medicos.Medico', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return 'Consulta del paciente %s con el médico %s' % (self.paciente, self.medico)
    
