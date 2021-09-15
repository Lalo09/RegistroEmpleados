from django.shortcuts import render
from .models import Departamento
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )

from applications.departamento import models

class DepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    model = Departamento
    context_object_name = "departamentos"