# Generated by Django 3.1.1 on 2020-09-09 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aprende', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='imagen_banner',
        ),
    ]
