from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('detallesProyecto/<int:proyecto_id>/', views.detallesProyecto, name='detallesProyecto'),
    path('nuevaProyecto/', views.nuevaProyecto, name='nuevaProyecto'),  # Formulario para agregar proyecto
    path('listadoProyecto/', views.listadoProyecto, name='listadoProyecto'),  # Página con el listado de proyectos
    path('proyecto/<int:proyecto_id>/', views.detallesProyecto, name='detallesProyecto'),
    path('eliminarProyecto/<proyecto_id>/', views.eliminarProyecto, name='eliminarProyecto'),  # Eliminar proyecto
    path('editarProyecto/<proyecto_id>', views.editarProyecto, name='editarProyecto'),  # Editar proyecto
    path('procesarEdicionProyecto/', views.procesarEdicionProyecto, name='procesarEdicionProyecto'),  # Procesar edición de proyecto
    path('agregarTarea/<int:proyecto_id>/', views.agregarTarea, name='agregarTarea'),
    path('editarProyecto/<int:proyecto_id>/', views.editarProyecto, name='editarProyecto'),  # Editar proyecto
      path('nuevaTarea/<int:proyecto_id>/', views.nuevaTarea, name='nuevaTarea'),  # Nuevo para agregar tareas
]

