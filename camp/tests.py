from __future__ import absolute_import
from __future__ import unicode_literals

from django.test import TestCase

from . import factories
from .forms import ChefForm
from .views import _maintain_meal_requirements
from .models import MealShift

class ChefRequirementsTestCase(TestCase):
    def setUp(self):
        self.event = factories.EventFactory()

    def _make_form(self, meal, need_courier, sous, kp):
        form = ChefForm(meal=meal, data={
            'need_courier': need_courier,
            'number_of_sous': sous,
            'number_of_kp': kp
        })
        if not form.is_valid():
            import pdb;pdb.set_trace()
            raise ValueError()
        return form

    def test_initial_requirements(self):
        meal = factories.MealFactory(event=self.event)
        form = self._make_form(meal, True, 2, 3)

        _maintain_meal_requirements(meal, form)

        self.assertEqual(1,
            meal.shifts.filter(role=MealShift.Courier).count())
        self.assertEqual(2,
            meal.shifts.filter(role=MealShift.Sous_Chef).count())
        self.assertEqual(3,
            meal.shifts.filter(role=MealShift.KP).count())

    def test_revising_decrease(self):
        meal = factories.MealFactory(event=self.event)
        form = self._make_form(meal, True, 2, 3)

        _maintain_meal_requirements(meal, form)

        # assign a worker to a meal to ensure unfilled positions are
        #  removed first

        kp_shift = meal.shifts.filter(role=MealShift.KP).order_by('pk')[2]
        kp_shift.worker = factories.UserFactory()
        kp_shift.save()

        form = self._make_form(meal, False, 1, 1)

        _maintain_meal_requirements(meal, form)

        self.assertEqual(0,
            meal.shifts.filter(role=MealShift.Courier).count())
        self.assertEqual(1,
            meal.shifts.filter(role=MealShift.Sous_Chef).count())
        self.assertEqual(1,
            meal.shifts.filter(role=MealShift.KP).count())

        # the only kp shift left is the one that was already filled.
        self.assertTrue(meal.shifts.filter(pk=kp_shift.pk).exists())

    def test_revising_increase(self):
        meal = factories.MealFactory(event=self.event)
        form = self._make_form(meal, True, 1, 1)

        _maintain_meal_requirements(meal, form)

        form = self._make_form(meal, True, 2, 3)

        _maintain_meal_requirements(meal, form)

        self.assertEqual(1,
            meal.shifts.filter(role=MealShift.Courier).count())
        self.assertEqual(2,
            meal.shifts.filter(role=MealShift.Sous_Chef).count())
        self.assertEqual(3,
            meal.shifts.filter(role=MealShift.KP).count())
