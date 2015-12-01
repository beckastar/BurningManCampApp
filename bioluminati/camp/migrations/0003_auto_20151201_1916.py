# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0002_auto_20151201_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='bike_photo',
            field=models.ImageField(null=True, upload_to=b'bike_images', blank=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 1, 19, 15, 59, 935164, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item',
            field=models.CharField(default='bike', max_length=20, blank=True),
            preserve_default=False,
        ),
    ]
