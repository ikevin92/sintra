from django.urls import path, include  # importamos el include
from generales.views import Home
#importamos para el login
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 2. configuramos la ruta despues de hacerlo en el urls de cursodj
    path('', Home.as_view(), name='home'),
    #enrutamiento login
  
]