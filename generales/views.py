# importar MIXIN para permisos de usuarios
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# import del reverselay
from django.urls import reverse_lazy
# a modo de ejemplo
from django.views import generic

from .models import *
from noticias.models import *

# Create your views here.


class Home(generic.TemplateView):
    template_name = 'generales/home.html'  # viene a ejecutar esta plantilla


class Historia(generic.TemplateView):
    template_name = 'generales/historia.html'


def home(request):
    secciones = SeccionNoticia.objects.all()
    
    template = "generales/home.html"
    return render(request, template, {'secciones': secciones})


def listado(request):
    secciones = SeccionNoticia.objects.all()   
    
    return render(request, {'secciones': secciones})


def laudos(request):
    categorias= CategoriaConvencion.objects.all()
    convenciones = Convencion.objects.all()
    template = "generales/convenciones.html"
    return render(request, template, {'convenciones': convenciones,'categorias': categorias})



