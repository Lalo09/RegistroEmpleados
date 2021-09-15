from applications import departamento
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )

from .models import Empleado
#Forms
from .forms import EmpleadoForm

class InicioView(TemplateView):
    """Vista de carga de pagina de inicio"""
    template_name = 'inicio.html'

class CorrectView(TemplateView):
    template_name='correcto.html'

class ListarEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 3
    ordering = 'first_name'
    context_object_name = "empleados"
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword","")
        lista = Empleado.objects.filter(first_name__icontains=palabra_clave)
        return lista
        

class ListarEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = "empleados"
    model = Empleado


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = 'persona/detalle_empleado.html'
    """
    model = Empleado
    template = "persona/detalle_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context["titulo"] = 'Empleado'
        return context
    """
    
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['shortname']
        lista = Empleado.objects.filter(departamento__short_name=area)
        return lista

class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]

    success_url = reverse_lazy('empleados-admin')


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name='persona/delete.html'
    success_url = reverse_lazy('empleados-admin')


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    """
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar'
    ]
    """
    form_class = EmpleadoForm
    success_url = reverse_lazy('empleados-admin')
