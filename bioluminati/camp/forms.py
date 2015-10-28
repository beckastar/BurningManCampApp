from django import forms
from django.forms import ModelForm
from models import mealShifts
from django.core.exceptions import ValidationError

from .models import mealShifts


class MealForm(ModelForm):
		
	class Meta:
		model = mealShifts
		fields = '__all__'
	def clean(self):		
	    data = self.cleaned_data
	    #check whether data is present as your wish 
	    #if exists raise Validation error.
	    return super(MealForm, self).clean()