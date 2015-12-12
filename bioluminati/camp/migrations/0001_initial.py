# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BicycleMutationInventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('material', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('units', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bike_photo', models.ImageField(null=True, upload_to=b'bike_images', blank=True)),
                ('bike_name', models.CharField(max_length=30)),
                ('bike_size_inches', models.IntegerField()),
                ('owners_last_year_on_playa', models.IntegerField()),
                ('needs_repairs', models.BooleanField(default=False)),
                ('in_bike_pool_this_year', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('bike_owner', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item', models.CharField(max_length=20, blank=True)),
                ('needs_repairs', models.BooleanField(default=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MealShifts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('assigned', models.BooleanField(default=False)),
                ('day', models.IntegerField(choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')])),
                ('meal', models.CharField(max_length=10, choices=[(b'Breakfast', b'Breakfast'), (b'Dinner', b'Dinner')])),
                ('shift', models.CharField(default=b'KP', max_length=10, choices=[(b'Chef', b'Chef'), (b'Sous-Chef', b'Sous_Chef'), (b'KP', b'KP')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('camper', models.ForeignKey(default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('has_ticket', models.BooleanField(default=False)),
                ('has_extra_ticket', models.BooleanField(default=False)),
                ('number_of_extra_tickets', models.IntegerField(default=0)),
                ('needs_ticket_for_self', models.BooleanField(default=False)),
                ('needs_ticket_for_friends', models.BooleanField(default=False)),
                ('number_of_extra_tickets_needed', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('camper', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playa_name', models.CharField(max_length=20)),
                ('website', models.CharField(max_length=20, blank=True)),
                ('picture', models.ImageField(upload_to=b'profile_images', blank=True)),
                ('city', models.CharField(max_length=20)),
                ('number_of_burns', models.IntegerField()),
                ('years_with_bio', models.IntegerField()),
                ('petronus', models.CharField(max_length=20, blank=True)),
                ('needs_camp_bike', models.BooleanField(default=False)),
                ('twitter_handle', models.CharField(max_length=30, blank=True)),
                ('facebook_name', models.CharField(max_length=30)),
                ('favorite_nonfiction', models.CharField(max_length=50)),
                ('favorite_fiction', models.CharField(max_length=50, blank=True)),
                ('favorite_movie', models.CharField(max_length=50, blank=True)),
                ('playa_hope', models.CharField(max_length=25, blank=True)),
                ('playa_fear', models.CharField(max_length=25, blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='mealshifts',
            unique_together=set([('day', 'meal', 'shift')]),
        ),
    ]
