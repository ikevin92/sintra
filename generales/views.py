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
    
    categorias = CategoriaConvencion.objects.all()
    convenciones = Convencion.objects.all()
    secciones = SeccionNoticia.objects.all()
    template = "generales/convenciones.html"
    return render(request, template, {'convenciones': convenciones, 'categorias': categorias,'secciones': secciones})


def estatutos(request):
    secciones = SeccionNoticia.objects.all()
    template = "generales/estatutos.html"
    return render(request, template, {'secciones': secciones})

def junta(request):
    secciones = SeccionNoticia.objects.all()
    template = "generales/junta-directiva.html"
    return render(request, template, {'secciones': secciones})

def comunicados(request):
    secciones = SeccionNoticia.objects.all()
    template = "generales/comunicados.html"
    return render(request, template, {'secciones': secciones})

def formatos(request):
    secciones = SeccionNoticia.objects.all()
    template = "generales/formato.html"
    return render(request, template, {'secciones': secciones})

def subdirectivas(request):
    secciones = SeccionNoticia.objects.all()
    template = "generales/subdirectivas.html"
    return render(request, template, {'secciones': secciones})


class Estatutos(generic.TemplateView):
    template_name = 'generales/estatutos.html'


class JuntaDirectiva(generic.TemplateView):
    template_name = 'generales/junta-directiva.html'


class Comunicados(generic.TemplateView):
    template_name = 'generales/comunicados.html'


class Formatos(generic.TemplateView):
    template_name = 'generales/formato.html'


class Subdirectivas(generic.TemplateView):
    template_name = 'generales/subdirectivas.html'
