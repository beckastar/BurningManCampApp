
from django.core.management.base import BaseCommand
from django.utils.encoding import smart_str
from datetime import datetime, timedelta
from camp.models import Event, Meal, User, MealShift, BikeMutationSchedule, PYB_shifts
# FIXME: gross, fix 2 kinds of undetermined.
from camp.models import undetermined, UNDETERMINED

import csv



def _parse_date(value):
    year, month, day = map(int, value.split('-'))

    return datetime(year, month, day)

class Command(BaseCommand):
    help = "Sets up a new event/year"

    def add_arguments(self, parser):
        parser.add_argument('start_date', action="store", type=_parse_date, help="in YYYY-MM-DD format")
        parser.add_argument('num_days', action="store", type=int, help="How long is this event?")
        parser.add_argument('--noinput', '--no-input',
            action='store_false', dest='interactive', default=True,
            help='Do NOT prompt the user for input of any kind.')

    def handle(self, **options):
        start_date = options['start_date']
        num_days = options['num_days']
        interactive = options['interactive']
        end_date = start_date + timedelta(days=num_days)

        event_name = "Burning Man %s" % start_date.year
        if Event.objects.filter(name=event_name).exists():
            if interactive:
                response = raw_input("%s exists - overwrite? (y/N) " % event_name)
            else:
                raise ValueError("Event %s exists, won't overwrite w/o input." % event_name)
            if response.strip().lower() != 'y':
                print "Not overwriting the existing event"
                return

            Event.objects.filter(name=event_name).delete()

        event = Event.objects.create(name=event_name,
            start_date=start_date, end_date=end_date)

        for i in range(num_days):
            day = start_date + timedelta(days=i)
            for kind, _ in Meal.Kinds:
                # FIXME: midnight bbqs shouldn't be every day, rather core tuesday - sat.
                # FIXME: shouldn't create chef shifts since they are on the meal.chef fk.
                meal = Meal.objects.create(event=event, day=day, kind=kind)
                # Each meal needs a chef, who will define further shift needs.
                MealShift.objects.create(meal=meal, role=MealShift.Chef)

            if day.weekday() in range(4): # (monday through thursday)
                for kind, _ in PYB_shifts:
                    for i in range(4):
                        BikeMutationSchedule.objects.create(event=event, date=day, shift=kind)

        Shelter.objects.update(sleeping_arrangement=undetermined)
        Vehicle.objects.update(transit_arrangement=UNDETERMINED)
        # No need to reset shifts, as we keep old events and shifts (which are tied to events).

