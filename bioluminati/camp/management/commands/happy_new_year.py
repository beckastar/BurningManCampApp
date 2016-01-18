
from django.core.management.base import NoArgsCommand
from django.utils.encoding import smart_str
from datetime import datetime
from camp.models import *
import csv




class Command(NoArgsCommand):
    help = "Resets the following fields in the bioluminati camp application so that they can be entered afresh each year"

    args = "[camp]"

    def handle_noargs(self, **options):
        print "Hello, World!"
        shifts = MealShift.objects.all()
        campers = UserProfile.objects.all()
        print shifts
        for shift in shifts:
            print shift.assigned
            print shift.camper
            shift.camper=None
            shift.assigned=False
            shift.date = None
            print shifts
        for camper in campers:
            camper.has_ticket = False
            camper.looking_for_ticket = False
            camper.camping_this_year = False
            camper.arrival_day = None
            camper.departure_day = None
            camper.date = None

