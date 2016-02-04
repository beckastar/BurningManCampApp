# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0012_auto_20160121_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikemutationschedule',
            name='day',
            field=models.IntegerField(choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday')]),
        ),
    ]
