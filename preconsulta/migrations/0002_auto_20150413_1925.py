# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20150413_1920'),
        ('preconsulta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='creadopor',
        ),
        migrations.AddField(
            model_name='paciente',
            name='usuariocreacion',
            field=models.ForeignKey(related_name='paciente_usuario', default=1, to='userprofiles.UserProfile'),
            preserve_default=False,
        ),
    ]
