# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='performance',
            old_name='start_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='ticketsale',
            old_name='start_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='merchandise',
            name='image',
            field=models.URLField(default=datetime.datetime(2015, 2, 5, 8, 40, 24, 252000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performance',
            name='image',
            field=models.URLField(default=datetime.datetime(2015, 2, 5, 8, 40, 30, 285000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
