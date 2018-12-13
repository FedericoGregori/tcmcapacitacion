from django.shortcuts import get_object_or_404, render

from cursos.models import Clase

def clase(request, clase_id):

  clase = get_object_or_404(Clase, pk=clase_id)

  context = {
    'clase' : clase
  }

  return render(request, 'clases/clase.html', context)