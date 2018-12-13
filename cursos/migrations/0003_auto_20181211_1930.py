# Generated by Django 2.1.4 on 2018-12-11 22:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20181211_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Publicado'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Fecha de adhesión'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='photo_main',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Portada'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
