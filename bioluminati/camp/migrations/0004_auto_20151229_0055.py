# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0003_auto_20151229_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='tent_length_inches',
            field=models.CharField(default=None, max_length=25, blank=True, choices=[(b'one inch', b'one inch'), (b'two inches', b'two inches'), (b'three inches', b'three inches'), (b'four inches', b'four inches'), (b'five inches', b'five inches'), (b'six inches', b'six inches'), (b'seven inches', b'seven inches'), (b'eight inches', b'eight inches'), (b'nine inches', b'nine inches'), (b'ten inches', b'ten inches'), (b'eleven inches', b'eleven inches')]),
        ),
    ]
