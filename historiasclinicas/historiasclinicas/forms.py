from django import forms
from .models import HistoriaClinica
import requests


class HistoriaClinicaForm(forms.ModelForm):

    paciente = forms.ChoiceField(choices=[])
    codigo = forms.CharField(max_length=100, required=True)
    antecedentes = forms.CharField(max_length=100, required=False)
    alergias = forms.CharField(max_length=100, required=False)
    medicamentos = forms.CharField(max_length=100, required=False)
    procedimientos = forms.CharField(max_length=100, required=False)
    diagnosticos = forms.CharField(max_length=100, required=True)
    consultas = forms.CharField(max_length=100, required=True)

    
    def __init__(self, *args, **kwargs):
        super(HistoriaClinicaForm, self).__init__(*args, **kwargs)
        self.fields['paciente'].choices = self.get_pacientes()
        self.fields['paciente'].widget.attrs.update({'class': 'form-control'})

    def get_pacientes(self):
        r = requests.get('http://34.170.116.216:8080/pacientes/')
        pacientes = r.json()
        choices = []
        for paciente in pacientes:
            choices.append((paciente['nombre'], paciente['nombre']+'-'+paciente['documento']))
        return choices
    
    class Meta:
        model = HistoriaClinica

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
            'paciente': 'Paciente',
            'codigo': 'Codigo',
            'antecedentes': 'Antecedentes',
            'alergias': 'Alergias',
            'medicamentos': 'Medicamentos',
            'procedimientos': 'Procedimientos',
            'diagnosticos': 'Diagnosticos',
            'consultas': 'Consultas'
        }
