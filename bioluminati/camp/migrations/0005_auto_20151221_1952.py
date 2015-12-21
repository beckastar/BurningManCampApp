# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0004_auto_20151221_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='diet_lifestyle',
            field=models.CharField(blank=True, max_length=200, choices=[(b'Vegetarian', b'Vegetarian'), (b'Vegan', b'Vegan'), (b'Omnivore', b'Omnivore'), (b'Pescaterian', b'Pescaterian'), (b'Gluten_free', b'Gluten_free')]),
        ),
    ]
