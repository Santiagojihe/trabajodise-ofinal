# apps/courses/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from .models import Curso, Inscripcion
from apps.forums.models import ForoDiscusion

class CursoListView(ListView):
    model = Curso
    #template_name = "courses/curso_list.html" ############posible error here
    template_name = "courses/curso_list.html"
    context_object_name = "cursos"

class CursoDetailView(DetailView):
    model = Curso
    template_name = "courses/curso_detail.html"
    context_object_name = "curso"

@login_required
def inscribir_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)

    # Solo admin gestiona inscripciones (según tu dominio)
    if not request.user.is_authenticated or not getattr(request.user, "is_admin", lambda: False)():
        return redirect("curso_detail", pk=pk)

    estudiante_id = request.POST.get("estudiante_id")
    if estudiante_id:
        Inscripcion.objects.get_or_create(estudiante_id=estudiante_id, curso=curso)

    # Crear foro si no existe
    ForoDiscusion.objects.get_or_create(curso=curso)

    return redirect("curso_detail", pk=pk)
