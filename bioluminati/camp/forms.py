from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import mealShifts, UserProfile


class MealForm(ModelForm):
    def __init__(self, *args, **kwargs): 
        super(MealForm, self).__init__(*args, **kwargs)
        self.fields['camper'].required = False
        self.fields['assigned'].required = False
        self.fields['day'].required = True
        import pdb; pdb.set_trace()
        
    class Meta:
        model = mealShifts
        fields = ('assigned', 'day', 'meal', 'shift', 'camper')


#don't change signature of save function 
    # def save(commit):
    #     form = super(MealForm, self).save(commit=False)
    #     fields['assigned'] = True
    #     return form 

class UserForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())


    class Meta:
        model = User 
        fields = ('username', 'email', 'password') 

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture', 'city', 'number_of_burns', 'years_with_bio', 'petronus', 'needs_camp_bike', 'twitter_handle')



# class ChefForm(forms.Form):
# 	need_courier = form.BooleanField()
# 	number_of_sous = form.IntegerField(default=0)
# 	number_of_kp = form.IntegerField(default=0)

	# def save(self, *args, **kwargs):
	# 	... 