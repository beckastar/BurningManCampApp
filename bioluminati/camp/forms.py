from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import MealShifts, UserProfile, Bikes, BicycleMutationInventory, Inventory
 

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

        Restrictions = (
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
        fields = ('user','picture', 'city', 
                'needs_camp_bike', 'diet_lifestyle',
                'other_restrictions', 'arrival_day', 
                'departure_day', 'meal_restrictions')

        widgets = {
            'meal_restrictions': forms.widgets.CheckboxSelectMultiple(choices=Restrictions),
        }

class BikeForm(ModelForm):
    class Meta:
        model = Bikes
        fields = '__all__'

class BikeMaterialForm(ModelForm):
    class Meta:
        model = BicycleMutationInventory
        fields = '__all__'

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'
