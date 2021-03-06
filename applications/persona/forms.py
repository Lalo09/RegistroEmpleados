from django import forms
from django.forms import fields, widgets
from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades'
        )
        widgets = {
            'habilidades' : forms.CheckboxSelectMultiple()
        }