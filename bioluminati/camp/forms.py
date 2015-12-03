from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import mealShifts, UserProfile, Bikes, BicycleMutationInventory, Inventory
 

class UserForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())


    class Meta:
        model = User 
        fields = ('username', 'email', 'password') 

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture', 'city', 'number_of_burns', 'years_with_bio', 'petronus', 'needs_camp_bike', 'twitter_handle')


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
