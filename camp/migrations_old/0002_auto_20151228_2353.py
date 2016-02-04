# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='camper',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='has_ticket',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='looking_for_ticket',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='make_of_car',
            field=models.CharField(default=None, max_length=15, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='model_of_car',
            field=models.CharField(default=None, max_length=25, blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='parking_vehicle_at_camp',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='primary_driver_in_your_party',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='sleeping_arrangement',
            field=models.CharField(default=None, max_length=25, choices=[(b'bringing_own_tent', b'bringing own tent'), (b"sharing someone else's tent", b"sharing someone else's tent"), (b'using camp yurt', b'using_camp_yurt'), (b'sharing rv', b'sharing_rv'), (b'other', b'other')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tent_length_feet',
            field=models.CharField(default=None, max_length=25, blank=True, choices=[(b'three feet', b'three feet'), (b'four feet', b'four feet'), (b'five feet', b'five feet'), (b'six feet', b'six feet'), (b'seven feet', b'seven feet'), (b'eight feet', b'eight feet')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tent_length_inches',
            field=models.CharField(default=None, max_length=25, blank=True, choices=[(b'three feet', b'three feet'), (b'four feet', b'four feet'), (b'five feet', b'five feet'), (b'six feet', b'six feet'), (b'seven feet', b'seven feet'), (b'eight feet', b'eight feet')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tent_width_feet',
            field=models.CharField(default=None, max_length=25, blank=True, choices=[(b'three feet', b'three feet'), (b'four feet', b'four feet'), (b'five feet', b'five feet'), (b'six feet', b'six feet'), (b'seven feet', b'seven feet'), (b'eight feet', b'eight feet')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tent_width_inches',
            field=models.CharField(default=None, max_length=25, blank=True, choices=[(b'one inch', b'one inch'), (b'two inches', b'two inches'), (b'three inches', b'three inches'), (b'four inches', b'four inches'), (b'five inches', b'five inches'), (b'six inches', b'six inches'), (b'seven inches', b'seven inches'), (b'eight inches', b'eight inches'), (b'nine inches', b'nine inches'), (b'ten inches', b'ten inches'), (b'eleven inches', b'eleven inches')]),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type_of_car',
            field=models.CharField(default=None, max_length=25, blank=True, choices=[(b'RV', b'RV'), (b'sedan', b'sedan'), (b'small_suv', b'small_suv'), (b'large_suv', b'large_suv'), (b'x_large_suv', b'x_large_suv'), (b'small_pickup', b'small_pickup'), (b'large_pickup', b'large_pickup'), (b'rocket_ship', b'rocket_ship')]),
        ),
        migrations.DeleteModel(
            name='Tickets',
        ),
    ]
