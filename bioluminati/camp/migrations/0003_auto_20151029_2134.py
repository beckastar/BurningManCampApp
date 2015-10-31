# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0002_auto_20151029_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealshifts',
            name='camper',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
