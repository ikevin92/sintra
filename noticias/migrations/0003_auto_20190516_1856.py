# Generated by Django 2.2.1 on 2019-05-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0002_auto_20190516_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(upload_to='noticias', verbose_name='Imagen Noticia'),
        ),
    ]
