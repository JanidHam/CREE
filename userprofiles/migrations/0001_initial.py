# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula_profesional', models.CharField(max_length=50, blank=True)),
                ('foto_perfil', models.ImageField(upload_to=b'userprofiles/imagesProfiles', verbose_name=b'FotoPerfil')),
                ('user', models.OneToOneField(related_name='perfil_usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
