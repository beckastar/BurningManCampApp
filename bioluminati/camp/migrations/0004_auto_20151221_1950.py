# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0003_auto_20151221_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='playa_fear',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='playa_hope',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='diet_lifestyle',
            field=models.CharField(default=None, max_length=200, choices=[(b'Vegetarian', b'Vegetarian'), (b'Vegan', b'Vegan'), (b'Omnivore', b'Omnivore'), (b'Pescaterian', b'Pescaterian'), (b'Gluten_free', b'Gluten_free')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='other_restrictions',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='arrival_day',
            field=models.IntegerField(max_length=10, choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='departure_day',
            field=models.IntegerField(max_length=10, choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='meal_restrictions',
            field=models.CharField(blank=True, max_length=200, choices=[(b'Mammal', b'Mammal'), (b'Onions', b'Onions'), (b'Cilantro', b'Cilantro'), (b'Soy', b'Soy'), (b'Dairy', b'Dairy'), (b'Quinoa', b'Quinoa'), (b'Pork', b'Pork'), (b'Olives', b'Olives'), (b'Dairy', b'Dairy'), (b'Peppers', b'Peppers'), (b'Cucumber', b'Cucumber'), (b'Nightshades', b'Nightshades'), (b'Nuts', b'Nuts')]),
        ),
    ]
