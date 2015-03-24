# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preconsulta', '0002_auto_20150320_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviciocree',
            name='usuariobaja',
            field=models.ForeignKey(related_name='serivicio_usuario', blank=True, to='userprofiles.UserProfile'),
            preserve_default=True,
        ),
    ]
