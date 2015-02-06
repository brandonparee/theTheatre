# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='description',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
