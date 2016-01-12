# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0009_auto_20151231_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='notes',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='bikes',
            name='repair_needed',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'needs_wheel_or_hub', b'needs_wheel_or_hub'), (b'tube', b'tube'), (b'brake adjustment', b'brake adjustment'), (b'seat', b'seat'), (b'pedal', b'pedal'), (b'tire', b'tire'), (b'new_chain', b'new_chain'), (b'derailer', b'derailer'), (b'brake repair', b'brake repair'), (b'head tightening', b'head tightening'), (b'cable repair or lube', b'cable repair or lube'), (b'other', b'other')]),
        ),
        migrations.AddField(
            model_name='bikes',
            name='stored_in_truck',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bikes',
            name='owners_last_year_on_playa',
            field=models.IntegerField(default=1),
        ),
    ]
