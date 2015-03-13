# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('idUser', models.IntegerField(serialize=False, primary_key=True)),
                ('userName', models.CharField(unique=True, max_length=50, verbose_name=b'Usuario')),
                ('nombre', models.CharField(max_length=80, verbose_name=b'Nombre')),
                ('apellidoP', models.CharField(max_length=80, verbose_name=b'ApellidoPaterno')),
                ('apellidoM', models.CharField(max_length=80, verbose_name=b'ApellidoMaterno')),
                ('pictureProfile', models.ImageField(upload_to=b'imagesProfiles', verbose_name=b'PictureProfile')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
