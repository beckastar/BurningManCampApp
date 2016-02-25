from collections import defaultdict

from django import forms
from django.forms import Form, ModelForm
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from .models import (
    Bike, BicycleMutationInventory, BikeMutationSchedule, Inventory,
    Meal, MealShift, Shelter, User, Vehicle)

class ChefForm(forms.Form):
    MAX_WORKERS = [(i, i) for i in range(5)]

    def __init__(self, meal, **kwargs):
        super(ChefForm, self).__init__(**kwargs)
        self.url = reverse('chef_requirements', kwargs={'meal_id': meal.id})

    need_courier = forms.BooleanField(initial=False, required=False)
    number_of_sous = forms.ChoiceField(initial=0, choices=MAX_WORKERS)
    number_of_kp = forms.ChoiceField(initial=0, choices=MAX_WORKERS)
    private_notes = forms.CharField(required=False, max_length=100000, widget=forms.Textarea,
        help_text="Notes for yourself")
    public_notes = forms.CharField(required=False, max_length=100000, widget=forms.Textarea,
        help_text="Describe the meal and any details you'd like to share.")

    @classmethod
    def for_meal(cls, meal, data=None):
        prefix = "meal-%s" % meal.id

        role_counts = defaultdict(int)
        for shift in meal.shifts.all():
            role_counts[shift.role] += 1

        initial = {
          'need_courier': role_counts[MealShift.Courier] > 0,
          'number_of_sous': role_counts[MealShift.Sous_Chef],
          'number_of_kp': role_counts[MealShift.KP]
        }
        return ChefForm(data=data, initial=initial, prefix=prefix, meal=meal)

class UserForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(ModelForm):

    class Meta:
        Fish = "Fish"
        Mammal = "Mammal"
        Vegetarian = "Vegetarian"
        Omnivore = "Omnivore"
        Onions = "Onions"
        Cucumber = "Cucumber"
        Peppers = "Peppers"
        Gluten_free = "Gluten_free"
        Vegan = "Vegan"
        Shellfish = "Shellfish"
        Olives = "Olives"
        Pork = "Pork"
        Soy = "Soy"
        Dairy = "Dairy"
        Cilantro = "Cilantro"
        Quinoa = "Quinoa"
        Nightshades = "Nightshades"
        Nuts = "Nuts"
        Pescaterian = "Pescaterian"
        All_Meat = "All_Meat"
        Legumes = "Legumes"
        Shellfish= "Shellfish"
        Gluten = "Gluten"

        Restrictions = (
          (Legumes, "Legumes"),
          (Shellfish, "Shellfish"),
          (Gluten, "Gluten"),
          (All_Meat, "All_Meat"),
          (Fish, "Fish"),
          (Mammal, "Mammal"),
          (Onions, "Onions"),
          (Cilantro, "Cilantro"),
          (Soy, "Soy"),
          (Dairy, "Dairy"),
          (Quinoa, "Quinoa"),
          (Pork, "Pork"),
          (Olives, "Olives"),
          (Dairy, "Dairy"),
          (Peppers, "Peppers"),
          (Cucumber, "Cucumber"),
          (Nightshades, "Nightshades"),
          (Nuts, "Nuts")
        )

        model = User
        fields = (
          'picture', 'city', 'cell_number',
          'emergency_contact_name', 'emergency_contact_phone',
          'meal_restrictions', 'other_restrictions',
          'arrival_date', 'departure_date',
          'has_ticket',
          'looking_for_ticket', 'camping_this_year'
          )

        widgets = {
            'meal_restrictions': forms.widgets.CheckboxSelectMultiple(choices=Restrictions),
        }

class VehicleForm(ModelForm):
  class Meta:
    model = Vehicle
    fields = '__all__'

class ShelterForm(ModelForm):
  class Meta:
    model = Shelter
    fields = '__all__'

class BikeForm(ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'

class BikeMaterialForm(ModelForm):
    class Meta:
        model = BicycleMutationInventory
        fields = '__all__'

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

class BikeMutationScheduleForm(ModelForm):
    class Meta:
      model = BikeMutationSchedule
      fields = "__all__"
