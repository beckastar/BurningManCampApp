# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='arrival_day',
            field=models.IntegerField(default=1, choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='departure_day',
            field=models.IntegerField(default=1, choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='meal_restrictions',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
