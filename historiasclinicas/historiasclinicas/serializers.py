from rest_framework import serializers
from .historiasclinicas import models


class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "medicamentos",
            "procedimientos",
            "diagnosticos",
            "consultas",
            "paciente",
            "codigo",
            "fecha_creacion",
            "antecedentes",
            "alergias",
        )
        model = models.HistoriaClinica
