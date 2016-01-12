# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0006_bikemutationschedule_assigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikemutationschedule',
            name='day',
            field=models.IntegerField(max_length=25, choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday')]),
        ),
    ]
