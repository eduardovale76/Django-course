# Generated by Django 4.0.4 on 2022-04-12 19:59

import base.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', base.models.UserManager()),
            ],
        ),
    ]