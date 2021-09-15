from django.contrib import admin
from django.urls import path
from . import views

def DesdeApps(self):
    print("--app persona--")

urlpatterns = [
    #path('admin/', admin.site.urls),  
    path('persona/',DesdeApps),
    path('',views.InicioView.as_view(),name='inicio'),
    path('correcto',views.CorrectView.as_view(),name='correcto'),
    path('listar-empleados', views.ListarEmpleados.as_view(),name='listar-empleados'),
    path('detalle-empleado/<pk>/',views.EmpleadoDetailView.as_view(),name='detalle-empleado'),
    path('lista-by-area/<shortname>',views.ListByAreaEmpleado.as_view(),name='empleados_area'),
    path('lista-empleados-admin',views.ListarEmpleadosAdmin.as_view(),name='empleados-admin'),
    path('update-empleado/<pk>/',views.EmpleadoUpdateView.as_view(),name='modificar-empleado'),
    path('delete-empleado/<pk>/',views.EmpleadoDeleteView.as_view(),name='eliminar-empleado'),
    path('delete-empleado/<pk>/',views.EmpleadoDeleteView.as_view(),name='eliminar-empleado'),
    path('add-empleado/',views.EmpleadoCreateView.as_view(),name='agregar-empleado')
]