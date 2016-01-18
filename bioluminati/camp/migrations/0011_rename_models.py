# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0010_auto_20160107_2323'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mealShifts',
            new_name='MealShift',
        ),
        migrations.RenameModel(
            old_name='Bikes',
            new_name='Bike',
        ),

    ]


