from django.shortcuts import render, redirect
from django.http import HttpResponse
from models import mealShifts, UserProfile
from django.shortcuts import render_to_response, get_object_or_404
from forms import MealForm, UserProfileForm
from django.core.context_processors import csrf 
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin
import itertools

def index(request):
	shifts = mealShifts.objects.all()
	return render(request, "index.html", {'shifts':shifts})

def login(request):
    return render(request, 'login.html')

@login_required
def profile(request):
	profile = UserProfile.objects.all()
	username = None
	form = UserProfileForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			# save the form 
			profile = form.save(commit = False)
			profile.user = request.user
			profile.save()
			return redirect('profile')
		else:
			form = UserProfileForm()
	return render(request, "profile.html", RequestContext(request, {'form':form, 'profile': profile,},))
		# return render_to_response('profile.html', 
		# RequestContext(request, {'form':form,'profile':profile, 'username':username},))


@login_required(login_url='login.html')
def signup(request):
	shifts = mealShifts.objects.all().order_by('day')
	day_choices = range(0, 6)
	meal_choices = ['Breakfast', 'Dinner']
	shift_choices = ['Chef', 'Sous_Chef', 'KP']
	# shift_options = itertools.product(day_choices, meal_choices, shift_choices)
	# available_shift_choices = filter(lambda option: not mealShifts.objects.filter(day=option[0], meal=option[1], shift=option[2]), shift_options)
	# for template tables
	sundayShiftsAvail = mealShifts.objects.filter(day=0, assigned=False)
	sundayShiftsTaken = mealShifts.objects.filter(day=0, assigned=True)

	mondayShiftsAvail = mealShifts.objects.filter(day=1, assigned=False)
	mondayShiftsTaken = mealShifts.objects.filter(day=1, assigned=True)

	tuesdayShiftsAvail = mealShifts.objects.filter(day=2, assigned=True)
	tuesdayShiftsTaken = mealShifts.objects.filter(day=2, assigned=True)

	wednesdayShiftsAvail = mealShifts.objects.filter(day=3, assigned=False)
	wednesdayShiftsTaken = mealShifts.objects.filter(day=3, assigned=True)

	thursdayShiftsAvail = mealShifts.objects.filter(day=4, assigned=False)
	thursdayShiftsTaken = mealShifts.objects.filter(day=4, assigned=True)

	fridayShiftsAvail = mealShifts.objects.filter(day=5, assigned=False)
	fridayShiftsTaken = mealShifts.objects.filter(day=5, assigned=True)

	saturdayShiftsAvail = mealShifts.objects.filter(day=6, assigned=False)
	saturdayShiftsTaken = mealShifts.objects.filter(day=6, assigned=True)

	saturdayShiftsAvail = mealShifts.objects.filter(day=7, assigned=False)
	saturdayShiftsTaken = mealShifts.objects.filter(day=7, assigned=True)

	username = None
	context = RequestContext(request)
	if request.method == 'POST':
		form = MealForm(request.POST)
		if form.is_valid():
			shift = form.save(commit=False)
			shift.camper = request.user
			form.fields['assigned'] = True
			shift.save()
			return redirect('signup')
		else:
			print form.errors 
	else:
		form = MealForm()
	return render_to_response('signup.html', 
		RequestContext(request, {
				'form':form,'username':username, 'shifts':shifts,
				'sundayShiftsAvail':sundayShiftsAvail, 'sundayShiftsTaken':sundayShiftsTaken,  
				'mondayShiftsTaken':mondayShiftsTaken, 'mondayShiftsAvail':mondayShiftsAvail,  
				'tuesdayShiftsTaken':tuesdayShiftsTaken, 'tuesdayShiftsAvail':tuesdayShiftsAvail,  
				'wednesdayShiftsTaken':wednesdayShiftsTaken, 'wednesdayShiftsAvail':wednesdayShiftsAvail, 
				'thursdayShiftsTaken':thursdayShiftsTaken, 'thursdayShiftsAvail':thursdayShiftsAvail,  
				'fridayShiftsTaken':fridayShiftsTaken, 'fridayShiftsAvail':fridayShiftsAvail,  
				'saturdayShiftsTaken':saturdayShiftsTaken, 'saturdayShiftsAvail':saturdayShiftsAvail
				# "available_shift_choices":available_shift_choices
				},))

# def register(request):
#     if request.method == 'POST':
#         uf = UserForm(request.POST, prefix='user')
#         upf = UserProfileForm(request.POST, prefix='userprofile')
#         if uf.is_valid() * upf.is_valid():
#             user = uf.save()
#             userprofile = upf.save(commit=False)
#             userprofile.user = user
#             userprofile.save()
#             return django.http.HttpResponseRedirect('registration_complete.html')
#     else:
#         uf = UserForm(prefix='user')
#         upf = UserProfileForm(prefix='userprofile')
#     return django.shortcuts.render_to_response('register.html', 
#                                                dict(userform=uf,
#                                                     userprofileform=upf),
#                                                context_instance=django.template.RequestContext(request))


