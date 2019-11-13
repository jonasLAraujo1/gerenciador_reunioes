from django import forms
from .models import *
from datetime import date


class  DateInput(forms.DateInput):
    """docstring for  DateInput"""
    input_type = 'date'


class  TimeInput(forms.TimeInput):
    """docstring for  TimeInput"""
    input_type = 'time'


class FormAgendaReuniao(forms.ModelForm):
    tipo_reuniao = forms.ModelChoiceField(queryset=Tipo.objects.all())
    class Meta:
        model = Reuniao
        fields = ['tipo_reuniao','pauta','local','semestre']


class FormTipo(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['titulo', 'cor']


class FormData(forms.ModelForm):
    class Meta:
        model = Data
        widgets ={
        'dia':DateInput(),
        'inicio':TimeInput(),
        'fim':TimeInput()
        }
        fields = ['dia', 'inicio', 'fim']

# class FormProfile(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = '__all__'
#

class FormReuniao(forms.ModelForm):
    class Meta:
        model = Reuniao
        fields = ['tipo_reuniao','pauta','local','semestre','deliberacoes','observacoes']

