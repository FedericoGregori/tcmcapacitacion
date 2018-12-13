from django.contrib import admin
from .models import Curso
from .models import Clase

class ClaseAdmin(admin.ModelAdmin):
  list_display = ('title', 'course', 'is_published')
  list_filter = ('course',)
  list_editable = ('is_published',)
  list_per_page = 10

class CursoAdmin(admin.ModelAdmin):
  list_display = ('title', 'is_published')
  list_editable = ('is_published',)
  list_per_page = 10


admin.site.register(Curso, CursoAdmin)
admin.site.register(Clase, ClaseAdmin)
