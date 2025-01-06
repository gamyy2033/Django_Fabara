from django.db import models

# Create your models here.

#Estructura del modelo Estudiante
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del Proyecto")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega")
    estado = models.BooleanField(default=True, verbose_name="Estado")

    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    ultima_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    completado = models.BooleanField(default=False)  # Campo que indica si la tarea está completada
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)  # Estado de la tarea
    def __str__(self):
        return self.nombre