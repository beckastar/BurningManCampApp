from __future__ import absolute_import

from datetime import datetime, timedelta

import factory

from factory.django import DjangoModelFactory
from django.utils import timezone



class UserFactory(DjangoModelFactory):
    username = factory.Sequence(lambda n: "user%d" % n)
    email = factory.LazyAttribute(lambda o: "%s@example.com" % o.username)
    first_name = factory.Sequence(lambda n: "first%d" % n)
    last_name = factory.Sequence(lambda n: "first%d" % n)
    is_staff = False
    is_active = True
    date_joined = factory.LazyAttribute(lambda o: datetime.now(tz=timezone.utc))

    class Meta:
        model = 'camp.User'

class EventFactory(DjangoModelFactory):
    name = factory.Sequence(lambda n: "event %d" % n)
    start_date = factory.Sequence(lambda n: datetime.now(tz=timezone.utc))
    end_date = factory.LazyAttribute(lambda o: o.start_date + timedelta(days=7))

    class Meta:
        model = 'camp.Event'

class MealFactory(DjangoModelFactory):
    event = factory.SubFactory(EventFactory)
    day = factory.LazyAttribute(lambda o: o.event.start_date)
    kind = "Breakfast"

    class Meta:
        model = "camp.Meal"

class MealShiftFactory(DjangoModelFactory):
    meal = factory.SubFactory(MealFactory)
    role = 'sous-chef'

    class Meta:
        model = "camp.MealShift"
