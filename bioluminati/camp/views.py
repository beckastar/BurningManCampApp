from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import MealShifts, UserProfile, Bikes, Vehicle, Inventory, Shelter, BicycleMutationInventory, BikeMutationSchedule, Inventory
from django.shortcuts import render_to_response, get_object_or_404
from forms import UserProfileForm, VehicleForm, UserForm, BikeForm, BikeMaterialForm, InventoryForm, ShelterForm
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
import itertools

def index(request):
    shifts = MealShifts.objects.all()
    return render(request, "index.html", {'shifts': shifts})

def login(request):
    return render(request, 'login.html')

def about(request):
     return render_to_response('about.html', RequestContext(request))

def prep(request):
     return render_to_response('prep.html', RequestContext(request))

def campers(request):
    campers = UserProfile.objects.all()
    context_dict = {'campers':campers}
    return render_to_response('campers.html', RequestContext(request, context_dict))


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
    # model = MealShifts
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

    context_dict  = {
                'username':username, 'poss_shifts':poss_shifts,
                'sundayShiftsAvail':sundayShiftsAvail, 'sundayShiftsTaken':sundayShiftsTaken,  
                'mondayShiftsTaken':mondayShiftsTaken, 'mondayShiftsAvail':mondayShiftsAvail,  
                'tuesdayShiftsTaken':tuesdayShiftsTaken, 'tuesdayShiftsAvail':tuesdayShiftsAvail,  
                'wednesdayShiftsTaken':wednesdayShiftsTaken, 'wednesdayShiftsAvail':wednesdayShiftsAvail, 
                'thursdayShiftsTaken':thursdayShiftsTaken, 'thursdayShiftsAvail':thursdayShiftsAvail,  
                'fridayShiftsTaken':fridayShiftsTaken, 'fridayShiftsAvail':fridayShiftsAvail,  
                'saturdayShiftsTaken':saturdayShiftsTaken, 'saturdayShiftsAvail':saturdayShiftsAvail
                }
    return render_to_response('signup.html', 
        RequestContext(request, context_dict,))


@login_required
def profile(request):
    form = UserProfileForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
        else:
            print(messages.error(request, "Error"))
    return render(request, "profile.html", RequestContext(request, {'form': form, 'profile': profile,}))

@login_required
def vehicle(request):
    form = VehicleForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()
        else:
            print(messages.error(request, "Error"))
    return render(request, "vehicle.html", RequestContext(request, {'form': form, 'profile': profile,}))

@login_required
def shelter(request):
    form = ShelterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            shelter = form.save(commit=False)
            shelter.user = request.user
            shelter.save()
        else:
            print(messages.error(request, "Error"))
    return render(request, "shelter.html", RequestContext(request, {'form': form, 'profile': profile,}))




@staff_member_required
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

@staff_member_required
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
    # currently owner's last year is required. probably good to remove that field. 


def remove_items_from_bikemutation(request):
    if request.method == 'POST':
        form = BikeMaterialForm()
        materials = BicycleMutationInventory.objects.all()
        item_id = int(request.POST.get('item_id'))  #this line is the problem 
        item = BicycleMutationInventory.objects.get(id=item_id)       
        item.delete()
        return render_to_response('bikemutation.html', {
            'form':form, 'materials':materials
            }, RequestContext(request))

def edit_bikemutation(request):
    materials= BicycleMutationInventory.objects.all()
    
    item_id = int(
        request.POST.get('item_id',
            request.GET.get('item_id')))

    item = int(request.POST.get('item_id')) 

    form = BikeMaterialForm(instance=item)

    if request.method == 'POST':
        form = BikeMaterialForm(data=request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('bikemutation')

    context_dict = {
           'item_id':item_id, 'form':form, 'materials':materials
            }
    return render_to_response('bikemutation.html', context_dict, RequestContext(request))

# items getting into database....
def bikemutation(request):
    model = BicycleMutationInventory
    materials = BicycleMutationInventory.objects.all()
    if request.method == "POST":
        form = BikeMaterialForm(data = request.POST)
        if form.is_valid():
            form.save()
        else:
            print "FORM WASNT VALID!!! OH NO!!!!"
    else:
        form = BikeMaterialForm()
    context_dict = {'form':form, 'materials':materials}
    return render_to_response('bikemutation.html', context_dict, RequestContext(request))

def remove_items_from_truck(request):
    if request.method == 'POST':
        form = InventoryForm()
        truck_inventory = Inventory.objects.all()
        item_id = int(request.POST.get('item_id'))  #this line is the problem 
        item = Inventory.objects.get(id=item_id)       
        item.delete()
        return render_to_response('inventory.html', {
            'form':form, 'truck_inventory':truck_inventory, 
            }, RequestContext(request))

def edit_truck_inventory(request):
    truck_inventory = Inventory.objects.all()

    item_id = int(
        request.POST.get('item_id',
            request.GET.get('item_id')))

    item = int(request.POST.get('item_id')) 
    
    form = InventoryForm(instance=item)

    if request.method == 'POST':
        form = InventoryForm(data=request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('inventory')

    context_dict = {"item_id": item_id, 'form':form, "truck_inventory":truck_inventory}
   
    return render_to_response('inventory.html', context_dict, RequestContext(request))

def show_inventory_form(request):
    model = Inventory
    truck_inventory = Inventory.objects.all()
    if request.method == "POST":
        form = InventoryForm(data = request.POST)
        if form.is_valid():
            form.save()
    else:
        form = InventoryForm()
    context = RequestContext(request)
    return render_to_response('inventory.html', {
            'form':form, 'truck_inventory':truck_inventory, 
            }, RequestContext(request))

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


def signup_for_pyb_shift(request):
    if request.method == 'POST':
        shift_id = int(request.POST.get('shift_id'))

        shift = BikeMutationSchedule.objects.get(id=shift_id)
        if shift.camper is not None:
            raise ValueError
        shift.camper = request.user
        print "shift camper %s" %shift.camper
        shift.assigned = True
        shift.save()

    return show_pybsignup(request)


def remove_self_from_pyb_shift(request):
    if request.method == 'POST':
        shift_id = int(request.POST.get('shift_id'))
        shift = BikeMutationSchedule.objects.get(id=shift_id)
        if shift.camper == request.user:
            shift.camper = None
            shift.assigned = False
            shift.save()

    return show_pybsignup(request)

def show_pybsignup(request):
    user = request.user
    username = None
    poss_shifts = BikeMutationSchedule.objects.all().order_by('day')
    mondayShiftsAvail = BikeMutationSchedule.objects.filter(day=1, assigned=False)
    mondayShiftsTaken = BikeMutationSchedule.objects.filter(day=1, assigned=True)
    tuesdayShiftsAvail = BikeMutationSchedule.objects.filter(day=2, assigned=True)
    tuesdayShiftsTaken = BikeMutationSchedule.objects.filter(day=2, assigned=True)
    wednesdayShiftsAvail = BikeMutationSchedule.objects.filter(day=3, assigned=False)
    wednesdayShiftsTaken = BikeMutationSchedule.objects.filter(day=3, assigned=True)
    thursdayShiftsAvail = BikeMutationSchedule.objects.filter(day=4, assigned=False)
    thursdayShiftsTaken = BikeMutationSchedule.objects.filter(day=4, assigned=True)
    fridayShiftsAvail = BikeMutationSchedule.objects.filter(day=5, assigned=False)
    fridayShiftsTaken = BikeMutationSchedule.objects.filter(day=5, assigned=True)

    context_dict = {
        'username':username, 'poss_shifts':poss_shifts,
        'mondayShiftsTaken':mondayShiftsTaken, 'mondayShiftsAvail':mondayShiftsAvail,  
        'tuesdayShiftsTaken':tuesdayShiftsTaken, 'tuesdayShiftsAvail':tuesdayShiftsAvail,  
        'wednesdayShiftsTaken':wednesdayShiftsTaken, 'wednesdayShiftsAvail':wednesdayShiftsAvail, 
        'thursdayShiftsTaken':thursdayShiftsTaken, 'thursdayShiftsAvail':thursdayShiftsAvail,  
        'fridayShiftsTaken':fridayShiftsTaken, 'fridayShiftsAvail':fridayShiftsAvail,  
    }
    return render_to_response('bikemutationsignup.html', 
        RequestContext(request, context_dict,))

def calendarview(request):
    # campers present and meal restrictions
    sundayCampers = UserProfile.objects.exclude(arrival_day__gte=0).exclude(departure_day__lt=0)
    mondayCampers = UserProfile.objects.exclude(arrival_day__gte=1).exclude(departure_day__lt=1)
    tuesdayCampers = UserProfile.objects.exclude(arrival_day__gte=2).exclude(departure_day__lt=2)
    wednesdayCampers = UserProfile.objects.exclude(arrival_day__gte=3).exclude(departure_day__lt=3)
    thursdayCampers = UserProfile.objects.exclude(arrival_day__gte=4).exclude(departure_day__lt=4)
    fridayCampers = UserProfile.objects.exclude(arrival_day__gte=5).exclude(departure_day__lt=5)
    saturdayCampers = UserProfile.objects.exclude(arrival_day__gte=6).exclude(departure_day__lt=6)


    # mealshifts
    sundayShiftsTaken = MealShifts.objects.filter(day=0, assigned=True)
    mondayShiftsTaken = MealShifts.objects.filter(day=1, assigned=True)
    tuesdayShiftsTaken = MealShifts.objects.filter(day=2, assigned=True)
    wednesdayShiftsTaken = MealShifts.objects.filter(day=3, assigned=True)
    thursdayShiftsTaken = MealShifts.objects.filter(day=4, assigned=True)
    fridayShiftsTaken = MealShifts.objects.filter(day=5, assigned=True)
    saturdayShiftsTaken = MealShifts.objects.filter(day=6, assigned=True)

    # bike shifts
    mondayBikeShifts = BikeMutationSchedule.objects.filter(day=1)
    tuesdayBikeShifts = BikeMutationSchedule.objects.filter(day=2)
    wednesdayBikeShifts = BikeMutationSchedule.objects.filter(day=3)
    thursdayBikeShifts = BikeMutationSchedule.objects.filter(day=4)
    fridayBikeShifts = BikeMutationSchedule.objects.filter(day=5)

    context_dict = {
    'sundayCampers':sundayCampers, 'mondayCampers':mondayCampers, 
    'tuesdayCampers':tuesdayCampers, 'wednesdayCampers':wednesdayCampers, 'thursdayCampers':thursdayCampers,
    'fridayCampers':fridayCampers, 'saturdayCampers':saturdayCampers, 
    'sundayShiftsTaken':sundayShiftsTaken, 'mondayShiftsTaken':mondayShiftsTaken, 'tuesdayShiftsTaken':tuesdayShiftsTaken,
    'wednesdayShiftsTaken':wednesdayShiftsTaken,'thursdayShiftsTaken ':thursdayShiftsTaken, 'fridayShiftsTaken':fridayShiftsTaken, 
    'saturdayShiftsTaken ':saturdayShiftsTaken, 'mondayBikeShifts':mondayBikeShifts,'tuesdayBikeShifts':tuesdayBikeShifts,
    'wednesdayBikeShifts':wednesdayBikeShifts, 'thursdayBikeShifts':thursdayBikeShifts, 'fridayBikeShifts ':fridayBikeShifts 
    }
    return render_to_response('calendar.html', 
        RequestContext(request, context_dict,))

