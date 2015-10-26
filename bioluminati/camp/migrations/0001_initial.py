# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mealShifts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assigned', models.BooleanField(default=False)),
                ('day', models.CharField(default=b'Sunday', max_length=7, choices=[(b'Sunday', b'Sunday'), (b'Monday', b'Monday'), (b'Tuesday', b'Tuesday'), (b'Wednesday', b'Wednesday'), (b'Thursday', b'Thursday')])),
                ('meal', models.CharField(default=b'Breakfast', max_length=10, choices=[(b'Breakfast', b'Breakfast'), (b'Dinner', b'Dinner')])),
                ('shift', models.CharField(default=b'KP', max_length=10, choices=[(b'Chef', b'Chef'), (b'Sous-Chef', b'Sous_Chef'), (b'KP', b'KP')])),
                ('camper', models.CharField(default=b'none', max_length=30)),
            ],
        ),
    ]
