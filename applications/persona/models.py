from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad',max_length=50)

    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades"

    def __str__(self):
        return self.habilidad

class Empleado(models.Model):
    JOB_CHOICES = (
        ('0','Contador'),
        ('1','Administrador'),
        ('2','Economista'),
        ('3','IT'),
    )

    first_name =  models.CharField("Nombres", max_length=50)
    last_name = models.CharField("Apellido",max_length=60)
    job = models.CharField("Puesto",max_length=1,choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado',blank=True,null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name_plural = 'Personal'
        ordering = ['last_name']
        unique_together = ('first_name','last_name')

    def __str__(self):
        return self.last_name + '-' + self.first_name