# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0003_auto_20151029_2134'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='mealShifts',
            new_name='MealShift',
        ),
    ]
