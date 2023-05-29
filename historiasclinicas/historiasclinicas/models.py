from django.db import models

# from medicamentos.models import Medicamento
# from procedimientos.models import Procedimiento
# from diagnosticos.models import Diagnostico
# from consultas.models import Consulta
# from pacientes.models import Paciente


class HistoriaClinica(models.Model):
    # medicamentos = models.ForeignKey(Medicamento, on_delete=models.CASCADE, null=True)
    # procedimientos = models.ForeignKey(
    #     Procedimiento, on_delete=models.CASCADE, null=True
    # )
    # diagnosticos = models.ForeignKey(Diagnostico, on_delete=models.CASCADE, null=True)
    # consultas = models.ForeignKey(Consulta, on_delete=models.CASCADE, null=True)
    # paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)

    medicamentos = models.CharField(max_length=50, null=True)
    procedimientos = models.CharField(max_length=50, null=True)
    diagnosticos = models.CharField(max_length=50, null=True)
    consultas = models.CharField(max_length=50, null=True)
    paciente = models.IntegerField(null=False, default=None)

    codigo = models.CharField(max_length=50, default="0")
    fecha_creacion = models.DateField(auto_now_add=True)
    antecedentes = models.CharField(max_length=400, null=True)
    alergias = models.CharField(max_length=400)

    def __str__(self):
        return "Historia clinica del paciente %s." % (self.paciente)
