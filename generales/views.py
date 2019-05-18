# importar MIXIN para permisos de usuarios
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# import del reverselay
from django.urls import reverse_lazy
# a modo de ejemplo
from django.views import generic

# Create your views here.

class Home(generic.TemplateView):
    template_name = 'generales/home.html'  # viene a ejecutar esta plantilla