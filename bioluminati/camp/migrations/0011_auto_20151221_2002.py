# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0010_auto_20151221_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='diet_lifestyle',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'Vegetarian', b'Vegetarian'), (b'Vegan', b'Vegan'), (b'Omnivore', b'Omnivore'), (b'Pescaterian', b'Pescaterian'), (b'Gluten_free', b'Gluten_free')]),
        ),
    ]
