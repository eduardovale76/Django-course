# Generated by Django 4.0.4 on 2022-05-12 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_aula_youtube_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='youtube_id',
            field=models.CharField(max_length=32),
        ),
    ]