# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0010_auto_20160107_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bikes',
            name='repair_needed',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'nothing', b'nothing'), (b'needs_wheel_or_hub', b'needs_wheel_or_hub'), (b'tube', b'tube'), (b'brake adjustment', b'brake adjustment'), (b'seat', b'seat'), (b'pedal', b'pedal'), (b'tire', b'tire'), (b'new_chain', b'new_chain'), (b'derailer', b'derailer'), (b'brake repair', b'brake repair'), (b'head tightening', b'head tightening'), (b'cable repair or lube', b'cable repair or lube'), (b'other', b'other')]),
        ),
    ]
