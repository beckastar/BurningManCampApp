# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camp', '0004_auto_20151229_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeMutationSchedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shift', models.CharField(max_length=25, choices=[(b'Morning', b'Morning'), (b'Afternoon', b'Afternoon')])),
                ('day', models.CharField(max_length=25, choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday')])),
                ('camper', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
