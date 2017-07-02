
from django.core.management.base import BaseCommand
from django.db.transaction import atomic
from django.utils.encoding import smart_str
from datetime import datetime, timedelta
from camp.models import (Event, Meal, User, MealShift, BikeMutationSchedule, PYB_shifts,
        Shelter, Vehicle)
# FIXME: gross, fix 2 kinds of undetermined.
from camp.models import undetermined, UNDETERMINED

import csv



def _parse_date(value):
    year, month, day = map(int, value.split('-'))

    return datetime(year, month, day)

class Command(BaseCommand):
    help = "Sets up a new event/year"

    def add_arguments(self, parser):
        parser.add_argument('earliest_arrival', action="store", type=_parse_date, help="in YYYY-MM-DD format")
        parser.add_argument('latest_departure', action="store", type=_parse_date, help="in YYYY-MM-DD format")
        # bbq is typically tues-sat of core week
        parser.add_argument('earliest_bbq', action="store", type=_parse_date, help="in YYYY-MM-DD format")
        parser.add_argument('latest_bbq', action="store", type=_parse_date, help="in YYYY-MM-DD format")
        # bms is typically mon-thurs of core week
        parser.add_argument('earliest_bms', action="store", type=_parse_date, help="in YYYY-MM-DD format")
        parser.add_argument('latest_bms', action="store", type=_parse_date, help="in YYYY-MM-DD format")

        parser.add_argument('--noinput', '--no-input',
            action='store_false', dest='interactive', default=True,
            help='Do NOT prompt the user for input of any kind.')

    def handle(self, **options):
        o = options

        interactive = o['interactive']

        arrival_date = o['earliest_arrival']
        event_name = "Burning Man %s" % arrival_date.year
        if Event.objects.filter(name=event_name).exists():
            if interactive:
                response = raw_input("%s exists - overwrite? (y/N) " % event_name)
            else:
                raise ValueError("Event %s exists, won't overwrite w/o input." % event_name)
            if response.strip().lower() != 'y':
                print "Not overwriting the existing event"
                return

            Event.objects.filter(name=event_name).delete()

        num_days = (o['latest_departure'] - o['earliest_arrival']).days
        with atomic():
            start_date = o['earliest_arrival']
            event = Event.objects.create(name=event_name,
                start_date=start_date, end_date=o['latest_departure'])

            # no meals on the first and last days
            for i in range(1, num_days - 1):
                day = start_date + timedelta(days=i)
                for kind, _ in Meal.Kinds:
                    if kind == Meal.Midnight:
                        if day < o['earliest_bbq'] or o['latest_bbq'] < day:
                            continue

                    meal = Meal.objects.create(event=event, day=day, kind=kind)
                    # Each meal needs a chef, who will define further shift needs.
                    MealShift.objects.create(meal=meal, role=MealShift.Chef)

                if o['earliest_bms'] <= day <= o['latest_bms']:
                    for kind, _ in PYB_shifts:
                        for i in range(4):
                            BikeMutationSchedule.objects.create(event=event, date=day, shift=kind)

            Shelter.objects.update(sleeping_arrangement=undetermined)
            Vehicle.objects.update(transit_arrangement=UNDETERMINED)

