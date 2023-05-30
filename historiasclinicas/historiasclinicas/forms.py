from django import forms
from .models import HistoriaClinica
import requests


class HistoriaClinicaForm(forms.ModelForm):
    
    class Meta:
        model = HistoriaClinica
        def get_pacientes():
            r = requests.get('http://34.170.116.216:8080/pacientes/')
            pacientes = r.json()
            choices = []
            for paciente in pacientes:
                choices.append((paciente['_id'], paciente['nombre']+'-'+paciente['documento']))
            return choices

        def __init__(self, *args, **kwargs):
            super(HistoriaClinicaForm, self).__init__(*args, **kwargs)
            self.fields['paciente'].choices = self.get_pacientes()

        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'antecedentes': forms.TextInput(attrs={'class': 'form-control'}),
            'alergias': forms.TextInput(attrs={'class': 'form-control'}),
            'medicamentos': forms.TextInput(attrs={'class': 'form-control'}),
            'procedimientos': forms.TextInput(attrs={'class': 'form-control'}),
            'diagnosticos': forms.TextInput(attrs={'class': 'form-control'}),
            'consultas': forms.TextInput(attrs={'class': 'form-control'}),

        }



        fields = [
            'paciente',
            'codigo',
            'antecedentes',
            'alergias',
            'medicamentos',
            'procedimientos',
            'diagnosticos',
            'consultas',
            

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
