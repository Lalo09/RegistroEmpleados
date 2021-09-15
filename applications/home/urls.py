from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/',views.pruebaView.as_view()) 
]