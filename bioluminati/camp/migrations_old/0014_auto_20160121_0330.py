# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0013_auto_20160121_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikemutationschedule',
            name='day',
            field=models.IntegerField(),
        ),
    ]
