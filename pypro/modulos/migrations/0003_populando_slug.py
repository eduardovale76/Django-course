# Generated by Django 4.0.4 on 2022-05-09 22:43

from django.db import migrations
from django.utils.text import slugify

def popular_slug(apps, schema_editor):
    Modulo = apps.get_model('modulos', 'modulo')
    for modulo in Modulo.objects.all():
        modulo.slug = slugify(modulo.titulo)
        modulo.save()

class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_modulo_slug'),
    ]

    operations = [
        migrations.RunPython(popular_slug)
    ]