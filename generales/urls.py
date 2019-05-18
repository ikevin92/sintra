from django.urls import path, include  # importamos el include
from generales.views import *
#importamos para el login
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 2. configuramos la ruta despues de hacerlo en el urls de cursodj
    path('', home, name='home'),
    path('historia', Historia.as_view(), name='historia'),
    path('listado', listado, name='secciones'),
    path('convenciones', laudos, name='convenciones')
    #enrutamiento login
  
]