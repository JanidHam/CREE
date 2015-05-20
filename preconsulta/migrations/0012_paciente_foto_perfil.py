# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0011_expediente_iscincomil'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='foto_perfil',
            field=models.ImageField(upload_to=b'pacientes/imagesProfiles', verbose_name=b'FotoPerfil', blank=True),
            preserve_default=True,
        ),
    ]
