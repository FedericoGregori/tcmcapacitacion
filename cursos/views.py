from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from .models import Clase, Curso

@login_required
def cursos(request):
  cursos = Curso.objects.all()

  context = {
    'cursos' : cursos
  }
  return render(request, 'cursos/cursos.html', context)

@login_required
def curso(request, curso_id):
  clases = Clase.objects.order_by('list_date').filter(course_id=curso_id)
  curso = get_object_or_404(Curso, pk=curso_id)

  context = {
    'clases' : clases,
    'curso' : curso
  }

  return render(request, 'cursos/clases.html', context)

def docs(request):
  return render(request, 'cursos/docs.html')