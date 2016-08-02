from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.urlresolvers import reverse
from arrow.parser import ParserError

from .models import (
    Bike, BicycleMutationInventory, BikeMutationSchedule, Inventory,
    Meal, MealShift, Shelter, User, Vehicle)
from .models import ( #shelter
  sharing_someone_elses, bringing_own_tent, sleep_in_vehicle, SIZE_CHOICES)
from .models import ( #transit
  DRIVING, RIDING_WITH)

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
          'number_of_kp': role_counts[MealShift.KP],
          'public_notes': meal.public_notes,
          'private_notes': meal.private_notes,
        }
        return ChefForm(data=data, initial=initial, prefix=prefix, meal=meal)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



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

class UserProfileForm(forms.ModelForm):
    def clean_other_restrictions(self):
      return self.cleaned_data['other_restrictions'].strip()

    def clean(self):
      cleaned_data = super(UserProfileForm, self).clean()
      arr = cleaned_data.get('arrival_date')
      dept = cleaned_data.get('departure_date')
      if bool(arr) != bool(dept):
        raise ValidationError("If either arrival or departure are given, both must be given.")
      if dept:
        if arr > dept:
          raise ValidationError("Arrival date must be before departure date.")

    class Meta:

        model = User
        fields = (
          'first_name', 'last_name', 'playa_name',
          'sponsor',
          'picture', 'city', 'cell_number',
          'email',
          'emergency_contact_name', 'emergency_contact_phone',
          'meal_restrictions', 'other_restrictions',
          'arrival_date', 'departure_date',
          'has_ticket',
          'looking_for_ticket', 'camping_this_year', 'email',
          'public_notes'
          )

        widgets = {
            'meal_restrictions': forms.widgets.CheckboxSelectMultiple(),
            'arrival_date': forms.widgets.SelectDateWidget(),
            'departure_date': forms.widgets.SelectDateWidget()
        }

class VehicleForm(forms.ModelForm):
  def __init__(self, user=None, **kwargs):
    self.user = user
    super(VehicleForm, self).__init__(**kwargs)
    providers = User.objects.filter(vehicle__transit_arrangement=DRIVING
      ).exclude(vehicle__user=user) # can't share with self
    self.fields['transit_provider'].queryset = providers

  class Meta:
    model = Vehicle
    fields = (
      'transit_arrangement', 'transit_provider',
      'model_of_car', 'make_of_car',
      'width', 'length'
    )

  def clean(self):
    cleaned_data = super(VehicleForm, self).clean()
    if cleaned_data['transit_arrangement'] == DRIVING:
      if not (cleaned_data['model_of_car'] and cleaned_data['make_of_car']):
        raise ValidationError("Please supply your car's make and model if you are the primary driver in your party.")

    if cleaned_data['transit_arrangement'] == RIDING_WITH:
      if (not cleaned_data['transit_provider']):
        raise ValidationError("If you're riding with someone, you must tell us who.")

    return cleaned_data

class ShelterForm(forms.ModelForm):
  def __init__(self, user=None, **kwargs):
    self.user = user
    super(ShelterForm, self).__init__(**kwargs)

    providers = User.objects.exclude(shelter=None # declared a shelter
      ).exclude(shelter__sleeping_arrangement=sharing_someone_elses # not sharing
      ).exclude(shelter__user=user) # not yourself

    self.fields['shelter_provider'].queryset = providers

  def clean(self):
    cleaned_data = super(ShelterForm, self).clean()
    if cleaned_data['sleeping_arrangement'] == bringing_own_tent:
      # gotta tell us details of tent
      size_values = [value for name, value in SIZE_CHOICES]
      if not (cleaned_data.get('width') in size_values and
              cleaned_data.get('length') in size_values):
        raise ValidationError("If you're bringing your own tent, you must tell us how big it is.")
    elif cleaned_data['sleeping_arrangement'] == sharing_someone_elses:
      if cleaned_data.get('shelter_provider') is None:
        self.add_error('shelter_provider', "If you are sharing someone else's shelter, you must tell us who.")
    elif cleaned_data['sleeping_arrangement'] == sleep_in_vehicle:
      # you have to put in a vehicle.
      try:
        vehicle = self.user.vehicle
        if not vehicle.transit_arrangement == DRIVING:
          raise ValidationError("If you sleep in your vehicle, you must indicate that you are driving.")
      except ObjectDoesNotExist:
        raise ValidationError("If you sleep in your vehicle, you must tell us about it.")
    else: # whatever you want
      pass
    return cleaned_data

  class Meta:
    model = Shelter
    fields = (
        'sleeping_arrangement',
        'shelter_provider',
        'number_of_people_tent_sleeps', 'sleeping_under_ubertent',
        'width', 'length'
    )

class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = '__all__'

class BikeMaterialForm(forms.ModelForm):
    class Meta:
        model = BicycleMutationInventory
        fields = '__all__'

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

class BikeMutationScheduleForm(forms.ModelForm):
    class Meta:
      model = BikeMutationSchedule
      fields = "__all__"
