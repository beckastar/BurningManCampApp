# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0007_auto_20151229_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='final_meal_on_departure_day',
            field=models.CharField(default='Breakfast', max_length=25, choices=[(b'Breakfast', b'Breakfast'), (b'Dinner', b'Dinner')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_meal_on_arrival_day',
            field=models.CharField(default='Breakfast', max_length=25, choices=[(b'Breakfast', b'Breakfast'), (b'Dinner', b'Dinner')]),
            preserve_default=False,
        ),
    ]
