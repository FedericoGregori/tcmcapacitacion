from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from cursos.models import Clase

@login_required
def clase(request, clase_id):

  clase = get_object_or_404(Clase, pk=clase_id)

  context = {
    'clase' : clase
  }

  return render(request, 'clases/clase.html', context)