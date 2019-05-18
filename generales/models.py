from django.db import models

# Create your models here.


class CategoriaConvencion(models.Model):

    nombre = models.CharField(("Nombre"), max_length=50)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:    
        verbose_name = ("Categoria")
        verbose_name_plural = ("Categorias")   


class Convencion(models.Model):

    nombre = models.CharField(("Nombre"), max_length=50)
    archivo = models.FileField(upload_to='convensiones/')
    categoria = models.ForeignKey('CategoriaConvencion', verbose_name=("Seccion Noticia"),
                                  on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} : {}'.format(self.categoria.nombre, self.nombre)

    class Meta:    
        verbose_name = ("Convencion")
        verbose_name_plural = ("Convenciones")   