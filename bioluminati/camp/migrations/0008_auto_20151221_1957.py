# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0007_auto_20151221_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='diet_lifestyle',
            field=models.CharField(default=None, max_length=200, blank=True, choices=[(b'Vegetarian', b'Vegetarian'), (b'Vegan', b'Vegan'), (b'Omnivore', b'Omnivore'), (b'Pescaterian', b'Pescaterian'), (b'Gluten_free', b'Gluten_free')]),
        ),
    ]
