from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField

class Clase(models.Model):
  course = models.ForeignKey('Curso', on_delete=models.DO_NOTHING, verbose_name="Curso")

  title = models.CharField(verbose_name="Título", max_length=200)
  description = models.TextField(verbose_name="Descripción", blank=True)
  photo_main = models.ImageField(verbose_name="Foto", upload_to='photos/%Y/%m/%d/')
  pdf = models.FileField(verbose_name="PDF ", upload_to='pdfs/%Y/%m/%d/')
  is_published = models.BooleanField(verbose_name="Publicado", default=True)
  list_date = models.DateTimeField(verbose_name="Fecha de adhesión", default=datetime.now, blank=True)

  #Main field para mostrar en el admin dashboard
  def __str__(self):
    return self.title

class Curso(models.Model):
  title = models.CharField(verbose_name="Título", max_length=200)
  description = models.TextField(verbose_name="Descripción", blank=True)
  photo_main = models.ImageField(verbose_name="Portada", upload_to='photos/%Y/%m/%d/')
  is_published = models.BooleanField(verbose_name="Publicado", default=True)
  list_date = models.DateTimeField(verbose_name="Fecha de adhesión", default=datetime.now, blank=True)
  #Main field para mostrar en el admin dashboard
  def __str__(self):
    return self.title