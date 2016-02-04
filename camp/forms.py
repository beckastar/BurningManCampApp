from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import MealShift, UserProfile, Vehicle, Bike, Shelter, BicycleMutationInventory, Inventory, BikeMutationSchedule


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

        model = UserProfile
        fields = (
          'picture', 'city', 'cell_number',
          'email_address', 'emergency_contact_name', 'meal_restrictions',
          'emergency_contact_phone', 'other_restrictions',  'arrival_day',
          'departure_day',
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
