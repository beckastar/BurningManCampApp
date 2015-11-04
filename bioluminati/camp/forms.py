from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import MealShift, UserProfile


class MealForm(ModelForm):
    class Meta:
        model = MealShift
        fields = ('assigned', 'day', 'meal', 'shift')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
        exclude = ['user']

class ChefForm(forms.Form):
    need_courier = forms.BooleanField(initial=False)
    number_of_sous = forms.IntegerField(initial=0)
    number_of_kp = forms.IntegerField(initial=0)

    def save(self, *args, **kwargs):
        pass