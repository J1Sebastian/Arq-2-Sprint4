from django import forms
from .models import HistoriaClinica
import requests


class HistoriaClinicaForm(forms.ModelForm):
    class Meta:
        model = HistoriaClinica
        r = requests.get('http://34.170.116.216:8080/pacientes/')
        pacientes = r.json()
        choices = []
        for paciente in pacientes:
            choices.append((paciente['_id'], paciente['nombre']+'-'+paciente['documento']))

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'antecedentes': forms.TextInput(attrs={'class': 'form-control'}),
            'alergias': forms.TextInput(attrs={'class': 'form-control'}),
            'medicamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'procedimientos': forms.TextInput(attrs={'class': 'form-control'}),
            'diagnosticos': forms.TextInput(attrs={'class': 'form-control'}),
            'consultas': forms.TextInput(attrs={'class': 'form-control'}),
            'paciente': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }



        fields = [
            'codigo',
            'antecedentes',
            'alergias',
            'medicamentos',
            'procedimientos',
            'diagnosticos',
            'consultas',
            'paciente'

        ]

        labels = {
            'codigo': 'Codigo',
            'antecedentes': 'Antecedentes',
            'alergias': 'Alergias',
            'medicamentos': 'Medicamentos',
            'procedimientos': 'Procedimientos',
            'diagnosticos': 'Diagnosticos',
            'consultas': 'Consultas',
            'paciente': 'Paciente'

        }
