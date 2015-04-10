# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0003_auto_20150323_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='idUser',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='pictureProfile',
            field=models.ImageField(upload_to=b'imagesProfiles', verbose_name=b'PictureProfile', blank=True),
            preserve_default=True,
        ),
    ]
