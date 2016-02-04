# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camp', '0008_auto_20151229_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sleeping_arrangement', models.CharField(max_length=25, choices=[(b'bringing_own_tent', b'bringing own tent'), (b"sharing someone else's tent", b"sharing someone else's tent"), (b'using camp yurt', b'using_camp_yurt'), (b'sharing rv', b'sharing_rv'), (b'other', b'other')])),
                ('number_of_people_tent_sleeps', models.IntegerField()),
                ('sleeping_under_ubertent', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary_driver_in_your_party', models.BooleanField(default=False)),
                ('model_of_car', models.CharField(default=None, max_length=25, blank=True)),
                ('make_of_car', models.CharField(default=None, max_length=15, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='bikes',
            old_name='bike_size_inches',
            new_name='bike_frame_size_inches',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='diet_lifestyle',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='final_meal_on_departure_day',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='first_meal_on_arrival_day',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='make_of_car',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='model_of_car',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='needs_camp_bike',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='parking_vehicle_at_camp',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='primary_driver_in_your_party',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sleeping_arrangement',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='tent_length_feet',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='tent_length_inches',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='tent_width_feet',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='tent_width_inches',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='type_of_car',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='cell_number',
            field=models.CharField(default=10, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email_address',
            field=models.CharField(default='b@b.com', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emergency_contact_name',
            field=models.CharField(default='alice', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='emergency_contact_phone',
            field=models.CharField(default=123456, max_length=15),
            preserve_default=False,
        ),
    ]
