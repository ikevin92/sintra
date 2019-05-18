from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Convencion)
class Convensiondmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre', 'categoria')
    search_fields = ('pk', 'nombre', 'categoria')
    autocomplete_fields = ['categoria']

@admin.register(CategoriaConvencion)
class CategoriaConvensiondmin(admin.ModelAdmin):
    list_display = ('pk', 'nombre',)
    search_fields = ('pk', 'nombre')
 

