# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0003_estadocivil_parentesco'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajesCartaConsentimiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.CharField(max_length=255)),
                ('fechacreacion', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
