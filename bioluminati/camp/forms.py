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
        model = UserProfile
        fields = ('playa_name', 'picture', 'city', 
                'number_of_burns', 'years_with_bio', 
                'petronus', 'needs_camp_bike', 'twitter_handle', 
                'facebook_url', 'diet_lifestyle',
                'other_restrictions', 'arrival_day', 'departure_day', 'meal_restrictions')
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


        widgets = {
            'meal_restrictions': forms.widgets.CheckboxSelectMultiple(),
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
