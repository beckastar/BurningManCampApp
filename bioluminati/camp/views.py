from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import mealShifts, UserProfile, Bikes, Tickets, Inventory
from django.shortcuts import render_to_response, get_object_or_404
from forms import UserProfileForm, UserForm, BikeForm
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
import itertools


def index(request):
    shifts = mealShifts.objects.all()
    return render(request, "index.html", {'shifts': shifts})


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
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
        else:
            form = UserProfileForm()
    return render(request, "profile.html", RequestContext(request, {'form': form, 'profile': profile, },))

def signup_for_shift(shift_id, camper):
    shift = mealShifts.objects.get(pk=shift_id)
    if shift.camper is not None:
        raise ValueError
    shift.camper = camper
    shift.assigned = True
    shift.save()

def remove_self_from_shift(shift_id, camper):
    shift = mealShifts.objects.get(pk=shift_id)
    if shift.camper == user.username:
        import pdb; pdb.set_trace()
        shift.camper = None
        shift.save()


@login_required(login_url='login.html')
def signup(request):
    model = mealShifts
    user = request.user
    poss_shifts = mealShifts.objects.all().order_by('day')
    day_choices = range(0, 6)
    meal_choices = ['Breakfast', 'Dinner']
    shift_choices = ['Chef', 'Sous_Chef', 'KP']
    username = None
    shift = mealShifts.objects.all()

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
    
    if request.method == 'POST':
        shift_id = request.POST.get('shift_id')
        signup_for_shift(shift_id, request.user)
    else:
        pass
    return redirect('signup')

    context = RequestContext(request)
    return render_to_response('signup.html', 
        RequestContext(request, {
                'username':username, 'poss_shifts':poss_shifts,
                'sundayShiftsAvail':sundayShiftsAvail, 'sundayShiftsTaken':sundayShiftsTaken,  
                'mondayShiftsTaken':mondayShiftsTaken, 'mondayShiftsAvail':mondayShiftsAvail,  
                'tuesdayShiftsTaken':tuesdayShiftsTaken, 'tuesdayShiftsAvail':tuesdayShiftsAvail,  
                'wednesdayShiftsTaken':wednesdayShiftsTaken, 'wednesdayShiftsAvail':wednesdayShiftsAvail, 
                'thursdayShiftsTaken':thursdayShiftsTaken, 'thursdayShiftsAvail':thursdayShiftsAvail,  
                'fridayShiftsTaken':fridayShiftsTaken, 'fridayShiftsAvail':fridayShiftsAvail,  
                'saturdayShiftsTaken':saturdayShiftsTaken, 'saturdayShiftsAvail':saturdayShiftsAvail
                },))


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        profile_form = UserProfileForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

def bike_form(request):
    form = BikeForm(data = request.POST)
    model = Bikes
    bikes = Bikes.objects.all()
    if request.method == "POST":

        if form.is_valid():

            form.save(commit=False)
            return redirect('index')
    else:
        form = BikeForm()

    return render(request, 'bikes.html', {'form':form, 'bikes':bikes})


