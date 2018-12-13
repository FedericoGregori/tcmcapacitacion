from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.cursos, name='cursos'),
    path('<int:curso_id>', views.curso, name='clases'),
    path('docs', views.docs, name='docs'),
]
