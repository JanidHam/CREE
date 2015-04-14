# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='foto_perfil',
            field=models.ImageField(upload_to=b'userprofiles/imagesProfiles', verbose_name=b'FotoPerfil', blank=True),
            preserve_default=True,
        ),
    ]
