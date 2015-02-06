# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('image', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('date', models.CharField(max_length=200)),
                ('image', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
