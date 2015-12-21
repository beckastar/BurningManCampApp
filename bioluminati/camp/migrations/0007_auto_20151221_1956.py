# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0006_auto_20151221_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='arrival_day',
            field=models.IntegerField(choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='departure_day',
            field=models.IntegerField(choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')]),
        ),
    ]
