from django import forms
from django.forms import ModelForm
from models import mealShifts
from django.core.exceptions import ValidationError

from .models import mealShifts


class MealForm(ModelForm):
		
	class Meta:
		model = mealShifts
		fields = '__all__'
