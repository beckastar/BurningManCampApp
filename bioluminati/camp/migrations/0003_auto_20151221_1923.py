# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0002_auto_20151212_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='facebook_name',
            new_name='facebook_url',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_fiction',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_movie',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='favorite_nonfiction',
        ),
    ]
