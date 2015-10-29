from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import mealShifts, UserProfile


class MealForm(ModelForm):
	class Meta:
		model = mealShifts
		fields = '__all__'
	def clean(self):		
	    data = self.cleaned_data
	    #check whether data is present as your wish 
	    #if exists raise Validation error.
	    return super(MealForm, self).clean()

class UserForm(ModelForm):
    class Meta:
        model = User 
        fields = ('username', 'email', 'password') 

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
        exclude = ['user']

