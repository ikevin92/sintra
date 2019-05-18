from django.db import models
import datetime
from ckeditor.fields import RichTextField


class Noticia(models.Model):

    imagen = models.ImageField(
        ("Imagen Noticia"),
        upload_to='noticias'
    )
    titulo = models.CharField(
        ("Ingrese Titulo Noticia"),
        max_length=50
    )

    cuerpo = models.TextField(("Cuerpo Noticia"))
    seccion = models.ForeignKey('SeccionNoticia',
                                verbose_name=("Seccion Noticia"),
                                on_delete=models.CASCADE
                                )

    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.titulo

    class Meta:

        verbose_name = ("Noticia")
        verbose_name_plural = ("Noticia")


class SeccionNoticia(models.Model):

    nombreSeccion = models.CharField(
        ("Ingrese Nombre Seccion"),
        max_length=50
    )
    class Meta:

        verbose_name = ("SeccionNoticia")
        verbose_name_plural = ("SeccionNoticias")

    def __str__(self):
        return self.nombreSeccion
