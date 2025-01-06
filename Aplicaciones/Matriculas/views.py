from django.shortcuts import render, redirect
from .models import Proyecto,Tarea
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Vista para la página de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Vista para crear un nuevo proyecto
def nuevaProyecto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        fecha_entrega = request.POST.get('fecha_entrega')
        estado = request.POST.get('estado') == 'on'  # Si está marcado el checkbox, se guarda como True

        # Crear un nuevo proyecto
        nuevo_proyecto = Proyecto(nombre=nombre, descripcion=descripcion, fecha_entrega=fecha_entrega, estado=estado)
        nuevo_proyecto.save()

        return redirect('listadoProyecto')  # Redirigir al listado de proyectos después de guardar

    return render(request, 'nuevaProyecto.html')  # Renderizar el formulario para crear un nuevo proyecto

def detallesProyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    tareas = proyecto.tareas.all()
    total_tareas = tareas.count()
    tareas_completadas = tareas.filter(completado=True).count()  # Usar 'completado' en lugar de 'estado'
    
    progreso = (tareas_completadas / total_tareas * 100) if total_tareas > 0 else 0
    restante = 100 - progreso  # Calcula el porcentaje restante
    
    context = {
        'proyecto': proyecto,
        'tareas': tareas,
        'progreso': progreso,
        'restante': restante,
    }
    return render(request, 'detallesProyecto.html', context)

# Vista para mostrar el listado de proyectos
def listadoProyecto(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'listadoProyecto.html', {'proyectos': proyectos})

# Vista para eliminar un proyecto
def eliminarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    proyecto.delete()
    return redirect('listadoProyecto')

# Vista para editar un proyecto
def editarProyecto(request, proyecto_id):
    proyecto = Proyecto.objects.get(id=proyecto_id)
    if request.method == 'POST':
        proyecto.nombre = request.POST.get('nombre')
        proyecto.descripcion = request.POST.get('descripcion')
        proyecto.fecha_entrega = request.POST.get('fecha_entrega')
        proyecto.estado = request.POST.get('estado') == 'on'  # Si está marcado el checkbox, se guarda como True
        proyecto.save()

        return redirect('listadoProyecto')  # Redirigir al listado de proyectos después de editar

    return render(request, 'editarProyecto.html', {'proyecto': proyecto})

# Vista para procesar la edición del proyecto
def procesarEdicionProyecto(request):
    # Aquí podrías agregar lógica adicional si lo necesitas
    return HttpResponse("Edición procesada")


def editarProyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        proyecto.nombre = request.POST.get('nombre')
        proyecto.descripcion = request.POST.get('descripcion')
        proyecto.fecha_entrega = request.POST.get('fecha_entrega')
        proyecto.estado = request.POST.get('estado') == 'on'
        proyecto.save()

        return redirect('listadoProyecto')  # Redirigir al listado después de guardar

    return render(request, 'editarProyecto.html', {'proyecto': proyecto})


def agregarTarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Tarea.objects.create(proyecto=proyecto, nombre=nombre)
        return redirect('detallesProyecto', proyecto_id=proyecto.id)

    return render(request, 'agregarTarea.html', {'proyecto': proyecto})

def nuevaTarea(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        completado = request.POST.get('completado') == 'on'  # Se marca como True si el checkbox está marcado
        
        # Crear la nueva tarea
        tarea = Tarea(nombre=nombre, completado=completado, proyecto=proyecto)
        tarea.save()
        
        return redirect('detallesProyecto', proyecto_id=proyecto.id)

    return render(request, 'nuevaTarea.html', {'proyecto': proyecto})