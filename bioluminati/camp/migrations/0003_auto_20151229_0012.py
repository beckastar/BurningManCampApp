# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0002_auto_20151228_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='quantity',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='camping_this_year',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
