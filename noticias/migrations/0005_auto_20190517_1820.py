# Generated by Django 2.2.1 on 2019-05-17 18:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0004_auto_20190516_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(verbose_name='Cuerpo_Noticia'),
        ),
    ]
