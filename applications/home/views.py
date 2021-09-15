from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class pruebaView(TemplateView):
    template_name = 'home/prueba.html'