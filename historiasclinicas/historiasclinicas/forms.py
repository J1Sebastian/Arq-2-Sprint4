from django import forms
from models import HistoriaClinica

class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        fields = [
            'codigo',
            'antecedentes',
            'alergias',
            'medicamentos',
            'procedimientos',
            'diagnosticos',
            'consultas',
            'paciente',

        ]

        labels = {
            'codigo': 'Codigo',
            'antecedentes': 'Antecedentes',
            'alergias': 'Alergias',
            'medicamentos': 'Medicamentos',
            'procedimientos': 'Procedimientos',
            'diagnosticos': 'Diagnosticos',
            'consultas': 'Consultas',
            'paciente': 'Paciente',

        }
