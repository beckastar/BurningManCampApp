# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='bike_photo',
            field=models.ImageField(null=True, upload_to=b'bike_images'),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='item',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
