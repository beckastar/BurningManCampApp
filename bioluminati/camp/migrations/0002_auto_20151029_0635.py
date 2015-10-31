# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='mealshifts',
            name='day',
            field=models.CharField(default=b'Sunday', max_length=10, choices=[(b'Sunday', b'Sunday'), (b'Monday', b'Monday'), (b'Tuesday', b'Tuesday'), (b'Wednesday', b'Wednesday'), (b'Thursday', b'Thursday'), (b'Friday', b'Friday')]),
        ),
        migrations.AlterField(
            model_name='mealshifts',
            name='meal',
            field=models.CharField(default=b'Dinner', max_length=10, choices=[(b'Breakfast', b'Breakfast'), (b'Dinner', b'Dinner')]),
        ),
        migrations.AlterUniqueTogether(
            name='mealshifts',
            unique_together=set([('day', 'meal', 'shift')]),
        ),
    ]
