# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0005_bikemutationschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikemutationschedule',
            name='assigned',
            field=models.BooleanField(default=False),
        ),
    ]
