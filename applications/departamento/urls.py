from applications.departamento import views
from django.contrib import admin
from django.urls import path

def DesdeApps(self):
    print("--app departamento--")

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('departamento/',DesdeApps),
    path('departmaneto-lista/',views.DepartamentoListView.as_view(),name='departamento-list'),
]