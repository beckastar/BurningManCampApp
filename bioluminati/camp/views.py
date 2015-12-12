from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import MealShifts, UserProfile, Bikes, Tickets, Inventory, BicycleMutationInventory, Inventory
from django.shortcuts import render_to_response, get_object_or_404
from forms import UserProfileForm, UserForm, BikeForm, BikeMaterialForm, InventoryForm
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
    shifts = MealShifts.objects.all()
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
    return render(request, "profile.html", RequestContext(request, {'form': form, 'profile': profile,}))

def signup_for_shift(request):
    if request.method == 'POST':
        shift_id = int(request.POST.get('shift_id'))

        shift = MealShifts.objects.get(id=shift_id)
        if shift.camper is not None:
            raise ValueError
        shift.camper = request.user
        print "shift camper %s" %shift.camper
        shift.assigned = True
        shift.save()

    return show_signup_table(request)


def _initial_meal():
    return {
        'serving': 'bacon', # fix with chef stuff.
        'positions': {'Chef': [], 'KP': [], 'Sous-Chef': []}, 
        'restrictions': [],
        'num_served': 0
    } 

def _meal_time(shift):
    return (shift.day, shift.meal)

def _finalize_meal(meal, shift):
    people_that_day = UserProfile.objects.filter(arrival_day__lt=shift.day,  departure_day__gt=shift.day)
    restrictions = sorted(list(set([person.meal_restrictions for person in people_that_day])))
    meal['day'] = shift.day
    meal['meal'] = shift.meal
    meal['restrictions'] = restrictions
    meal['num_served'] = people_that_day.count()

def meal_schedule(request):
    shifts = MealShifts.objects.order_by('day', 'meal')
    shifts_by_meal = [] 
    # meal = {'serving': 'bacon', 'day': day, 'meal': 'breakfast'
    #   'positions': ['chef': "a", 'KP': [workers],...],
    #   'restrictions': ['avacado'] 
    #   'num_served': 25
    # }
    if shifts:
        first_shift = shifts[0]
        previous_meal = _meal_time(first_shift)
        meal = _initial_meal()
        meal_dirty = False
        for shift in shifts:
            meal_time = _meal_time(shift)
            if previous_meal != meal_time:
                _finalize_meal(meal, shift)
                shifts_by_meal.append(meal)
                meal = _initial_meal()
                meal_dirty = False

            meal_dirty = True
            meal['positions'][shift.shift].append(shift)

        if meal_dirty:
            _finalize_meal(meal, shift)
            shifts_by_meal.append(meal)        

    context_dict = {'shifts_by_meal': shifts_by_meal}
    return render(request, "meal_schedule.html", RequestContext(request, context_dict))

def remove_self_from_shift(request):
    if request.method == 'POST':
        shift_id = int(request.POST.get('shift_id'))
        shift = MealShifts.objects.get(id=shift_id)
        if shift.camper == request.user:
            shift.camper = None
            shift.assigned = False
            shift.save()

    return show_signup_table(request)
    
def show_signup_table(request):
    model = MealShifts
    user = request.user
    poss_shifts = MealShifts.objects.all().order_by('day')
    day_choices = range(0, 6)
    meal_choices = ['Breakfast', 'Dinner']
    shift_choices = ['Chef', 'Sous_Chef', 'KP']
    username = None
    shift = MealShifts.objects.all()

    sundayShiftsAvail = MealShifts.objects.filter(day=0, assigned=False)
    sundayShiftsTaken = MealShifts.objects.filter(day=0, assigned=True)
    mondayShiftsAvail = MealShifts.objects.filter(day=1, assigned=False)
    mondayShiftsTaken = MealShifts.objects.filter(day=1, assigned=True)
    tuesdayShiftsAvail = MealShifts.objects.filter(day=2, assigned=True)
    tuesdayShiftsTaken = MealShifts.objects.filter(day=2, assigned=True)
    wednesdayShiftsAvail = MealShifts.objects.filter(day=3, assigned=False)
    wednesdayShiftsTaken = MealShifts.objects.filter(day=3, assigned=True)
    thursdayShiftsAvail = MealShifts.objects.filter(day=4, assigned=False)
    thursdayShiftsTaken = MealShifts.objects.filter(day=4, assigned=True)
    fridayShiftsAvail = MealShifts.objects.filter(day=5, assigned=False)
    fridayShiftsTaken = MealShifts.objects.filter(day=5, assigned=True)
    saturdayShiftsAvail = MealShifts.objects.filter(day=6, assigned=False)
    saturdayShiftsTaken = MealShifts.objects.filter(day=6, assigned=True)

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


def remove_bike(request):
    if request.method == 'POST':
        form = BikeForm()
        bicycles = Bikes.objects.all()
        bike_id = int(request.POST.get('bike_id')) 
        bike = Bikes.objects.get(id=bike_id)
        bike.delete()
        return render_to_response('bikes.html', {
            'form':form, 'bicycles':bicycles, 
            }, RequestContext(request))

def edit_bike(request):
    bicycles = Bikes.objects.all()

    bike_id = int(
        request.POST.get('bike_id',
            request.GET.get('bike_id')))

    bike = Bikes.objects.get(id=bike_id)
    
    form = BikeForm(instance=bike)

    if request.method == 'POST':
        form = BikeForm(data=request.POST, instance=bike)

        if form.is_valid():
            form.save()
            return redirect('bikes')

    context_dict = {"bike_id": bike_id, 'form':form, "bicycles":bicycles}
    
    return render_to_response('bikes.html', context_dict, RequestContext(request))

# def save_bike(request):
#     if request.method == 'POST':
#         form = BikeForm()
#         bicycles = Bikes.objects.all()
#         bike_id = int(request.POST.get('bike_id')) 
#         bike = Bikes.objects.get(id=bike_id)
#         context_dict = {"bike_id": bike_id, 'form':form, "bicycles":bicycles}
#         if form.is_valid():
#             form.save()
#         return render_to_response('bikes.html', context_dict, RequestContext(request))
      


def show_bike_form(request):
    model = Bikes
    bicycles = Bikes.objects.all()
    
    if request.method == "POST":
        form = BikeForm(data = request.POST)
        if form.is_valid():
            form.save()

    else:
        form = BikeForm()
    context = RequestContext(request)
    return render_to_response('bikes.html', {
            'form':form, 'bicycles':bicycles, 
            }, RequestContext(request))


def bikemutation(request):
    model = BicycleMutationInventory
    materials = BicycleMutationInventory.objects.all()
    form = BikeMaterialForm(data = request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save()
        else:
            print "FORM WASNT VALID!!! OH NO!!!!"

    else:
        form = BikeMaterialForm()
    context_dict = {'form':form, 'materials':materials}
    return render_to_response('bikemutation.html', context_dict, RequestContext(request))


def delete_item(item_id):
    thing = Inventory.objects.get(pk=id)
    thing.item = ''
    thing.save()


def inventory(request, id):
    if request.method == "GET":
        stuff = Inventory.objects.get(id=id)
        form = InventoryForm(instance=stuff)

    if request.method == "POST":
        stuff = Inventory.objects.get(id=id)
        form = InventoryForm(data=request.POST, instance=stuff) 
        if form.is_valid():
            form.save()

    return render(request, 'inventory.html', {'form': form, 'stuff': stuff})


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
        return redirect('index')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response('register.html', 
        RequestContext(request, {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},))

def about(request):
     return render_to_response('about.html', RequestContext(request))


def profile_view(request, id):
    u = UserProfile.objects.get(pk=id)


