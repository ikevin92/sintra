from django.urls import path, include  # importamos el include
from .views import *
#importamos para el login
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 2. configuramos la ruta despues de hacerlo en el urls de cursodj
    path('noticias/', noticiasList, name='listado'),
    #enrutamiento login
  
]