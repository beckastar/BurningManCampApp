from django import forms
from django.forms import ModelForm
from models import mealShifts
from django.core.exceptions import ValidationError

from .models import mealShifts


class MealForm(ModelForm):
	day = forms.CharField(max_length = 100, widget=forms.Select()) 
		
	class Meta:
		model = mealShifts
		fields = ['day']

form = MealForm()

