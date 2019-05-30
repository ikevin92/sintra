from django.shortcuts import render, HttpResponse
from .models import *
from django.http import HttpResponseRedirect
from django.views.generic import *

# Create your views here.
class NoticiaListView(ListView):
    model = Noticia
    template_name = "noticias/listado.html"
    ordering = ('-creado')
    paginate_by = 3
    context_object_name='noticias'

def noticiasList(request, id_seccion):
    noticias= Noticia.objects.filter(seccion__pk=id_seccion)
    secciones = SeccionNoticia.objects.all()
    template = "noticias/listado.html"
    return render(request, template, {'noticias': noticias,'secciones': secciones})

def noticiaDetail(request, id_noticia):
    noticia= Noticia.objects.get(pk=id_noticia)
    print(id_noticia)
    print(noticia)
    secciones = SeccionNoticia.objects.all()
    template = "noticias/detalle.html"
    return render(request, template, {'noticia': noticia,'secciones': secciones})

  
