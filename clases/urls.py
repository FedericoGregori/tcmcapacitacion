from django.urls import path, include

from . import views

urlpatterns = [
    path('<int:clase_id>', views.clase, name='clase'),
]
