# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20150205_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='description',
            field=models.CharField(max_length=2000),
            preserve_default=True,
        ),
    ]
