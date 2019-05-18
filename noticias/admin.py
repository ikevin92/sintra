from django.contrib import admin
from .models import Noticia, SeccionNoticia

# Register your models here.
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'imagen', 'titulo', 'cuerpo','seccion')
    search_fields = ('pk', 'imagen', 'titulo', 'cuerpo','seccion')
    autocomplete_fields = ['seccion']

@admin.register(SeccionNoticia)
class SeccionNoticiaAdmin(admin.ModelAdmin):
    list_display = ('pk', 'nombreSeccion')
    search_fields = ('pk', 'nombreSeccion')
    