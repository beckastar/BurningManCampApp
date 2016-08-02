from __future__ import absolute_import

from collections import defaultdict
from itertools import groupby

from django.db.transaction import atomic
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context_processors import csrf
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages

from .shortcuts import get_current_event
from .models import Event, Meal, MealShift, User, Bike, Vehicle, Inventory, Shelter, BicycleMutationInventory, BikeMutationSchedule, Inventory
from .forms import UserProfileForm, VehicleForm, UserForm, BikeForm, BikeMaterialForm, InventoryForm, ShelterForm, ChefForm


@login_required
def meal_shifts(request):
    meals = Meal.objects.all().prefetch_related('shifts')

    return render(request, 'meal_shifts.html',
        {'meals':meals})

@login_required
def chef_signup(request, meal_id):
    if request.method != 'POST':
        raise Http404
    meal = get_object_or_404(Meal, pk=meal_id)
    if meal.chef_id != request.user.id:
        if meal.chef_id is not None:
            raise Http404("A chef is already assigned to that meal")
        # nobody is chef yet.
        meal.chef = request.user
    else:
        # step down from the meal
        meal.chef = None
    meal.save()

    return redirect('meal_shifts')

def _maintain_role_requirement(meal, role, needed):
    qs = MealShift.objects.filter(meal=meal, role=role)
    existing = qs.count()

    if existing == needed:
        return
    elif existing > needed:
        extra = existing - needed
        # prefer to get rid of unclaimed shifts.
        unassigned_pks = qs.filter(worker__isnull=True
            ).values_list('pk', flat=True)
        if len(unassigned_pks) > extra:
            # remove just some of the unassigned
            unassigned_pks = unassigned_pks[:extra]
        qs.filter(pk__in=unassigned_pks).delete()
        extra -= len(unassigned_pks)

        if extra > 0:
            # no choice but to delete assigned shifts. Do in order of PK,
            # which is roughly signup order.
            extra_pks = qs.order_by('-pk').values_list('pk', flat=True)[:extra]
            qs.filter(pk__in=extra_pks).delete()
    else: # existing < needed
        for i in range(needed - existing):
            MealShift.objects.create(meal=meal, role=role)

def _maintain_meal_requirements(meal, chef_form):
    # generate or remove shifts as required.
    need = 1 if chef_form.cleaned_data['need_courier'] else 0
    _maintain_role_requirement(meal, MealShift.Courier, need)

    _maintain_role_requirement(meal, MealShift.Sous_Chef,
        int(chef_form.cleaned_data['number_of_sous']))

    _maintain_role_requirement(meal, MealShift.KP,
        int(chef_form.cleaned_data['number_of_kp']))

    meal.private_notes = chef_form.cleaned_data['private_notes']
    meal.public_notes = chef_form.cleaned_data['public_notes']
    meal.save()

@login_required
def chef_requirements(request, meal_id):
    if request.method != 'POST':
        raise Http404()
    meal = get_object_or_404(Meal, pk=meal_id)
    if meal.chef_id != request.user.id:
        raise Http404("Can not edit requirements if you're not chef.")

    requirements = ChefForm.for_meal(meal=meal, data=request.POST)

    if not requirements.is_valid():
        return render(request, "meals/chef_requirements.html", {"meal": meal, "form": requirements})

    with atomic():
        _maintain_meal_requirements(meal, requirements)

    return redirect('meal_shifts')

@login_required
def worker_signup(request, shift_id):
    if request.method != 'POST':
        raise Http404
    shift = get_object_or_404(MealShift, pk=shift_id)

    if shift.worker_id != request.user.id:
        if shift.worker_id is not None:
            raise ValueError("A worker is already working that shift.")
        # nobody is signed up yet.
        shift.worker = request.user
    else:
        # step down from the shift.
        shift.worker = None
    shift.save()

    return redirect('meal_shifts')

def index(request):
    shifts = MealShift.objects.all()
    return render(request, "index.html", {'shifts': shifts})

def login(request):

    username = request.POST['username']

    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('profile')
        # else:
            # Return a 'disabled account' error message
                # else:
        # Return an 'invalid login' error message.

    return render(request, 'login.html')

def about(request):
     return render_to_response('about.html', RequestContext(request))

def prep(request):
     return render_to_response('prep.html', RequestContext(request))

def campers(request):
    campers = User.objects.all().prefetch_related('meal_restrictions')

    for camper in campers:
        camper.restrictions = ", ".join(map(str, camper.meal_restrictions.all())) or "None"

    context_dict = {'campers':campers}
    return render_to_response('campers.html', RequestContext(request, context_dict))


def _initial_meal(meal):
    people_that_day = User.objects.filter(
        arrival_date__lte=meal.day,  departure_date__gte=meal.day
        ).prefetch_related('meal_restrictions')

    other_restrictions = []
    people_by_restriction = defaultdict(list)
    for camper in people_that_day:
        if camper.other_restrictions:
            other_restrictions.append(camper.other_restrictions)
        for restriction in camper.meal_restrictions.all():
            people_by_restriction[restriction.name].append(camper.display_name)
    if other_restrictions:
        other_restrictions = ", ".join(other_restrictions)

    for restriction in people_by_restriction:
        people_by_restriction[restriction].sort()

    positions = {
        role_display: []
        for role_code, role_display in MealShift.Roles
        if role_code != MealShift.Chef
    }

    return {
        'day': meal.day,
        'chef': meal.chef,
        'meal': meal.kind,
        'serving': meal.public_notes,
        'positions': positions,
        'restrictions': people_by_restriction,
        'other_restrictions': other_restrictions,
        'num_served': people_that_day.count()
    }


def meal_schedule(request):
    # FIXME: maybe urls should include the event they are related to?
    event = get_current_event()

    shifts_by_meal = []
    for meal in Meal.objects.filter(event=event):
        meal_summary = _initial_meal(meal)

        for shift in meal.shifts.all().prefetch_related('worker'):
            if shift.role != MealShift.Chef:
                meal_summary['positions'][shift.get_role_display()].append(shift)

        shifts_by_meal.append(meal_summary)

    print shifts_by_meal[0]['restrictions'].items()
    context_dict = {'shifts_by_meal': shifts_by_meal}
    return render(request, "meal_schedule.html", context_dict)

@login_required
def profile(request):
    form = UserProfileForm(instance=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    return render(request, "profile.html", RequestContext(request, {'form': form, 'profile': profile,}))

@login_required
def vehicle(request):
    try:
        instance = Vehicle.objects.get(user=request.user)
    except Vehicle.DoesNotExist:
        instance = None

    form = VehicleForm(user=request.user, instance=instance)
    if request.method == 'POST':
        post_data = request.POST
        form = VehicleForm(user=request.user, data=post_data, instance=instance)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.user = request.user
            vehicle.save()

            return redirect('vehicle')

    return render(request, "vehicle.html", RequestContext(request, {'form': form, 'profile': profile,}))

@login_required
def shelter(request):
    try:
        shelter = Shelter.objects.get(user=request.user)
    except Shelter.DoesNotExist:
        shelter = None

    form = ShelterForm(user=request.user, instance=shelter)
    if request.method == 'POST':
        form = ShelterForm(user=request.user, data=request.POST, instance=shelter)
        if form.is_valid():
            shelter = form.save(commit=False)
            shelter.user = request.user
            shelter.save()

            return redirect('shelter')

    return render(request, "shelter.html", RequestContext(request, {'form': form}))

@staff_member_required
def remove_bike(request):
    if request.method == 'POST':
        form = BikeForm()
        bicycles = Bike.objects.all()
        bike_id = int(request.POST.get('bike_id'))
        bike = Bike.objects.get(id=bike_id)
        bike.delete()
        return render_to_response('bikes.html', {
            'form':form, 'bicycles':bicycles,
            }, RequestContext(request))

@staff_member_required
def edit_bike(request, bike_id):
    bike = Bike.objects.get(id=bike_id)
    form = BikeForm(instance=bike)

    if request.method == 'POST':
        form = BikeForm(data=request.POST, instance=bike)

        if form.is_valid():
            form.save()
            return redirect('bikes')

    context_dict = {'form':form}
    return render_to_response('edit_bike.html', context_dict, RequestContext(request))

def show_bike_form(request):
    bicycles = Bike.objects.all()

    if request.method == "POST":
        form = BikeForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('bikes')

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

@login_required
def bms_worker_signup(request, shift_id):
    if request.method != 'POST':
        raise Http404

    shift = get_object_or_404(BikeMutationSchedule, pk=shift_id)

    if shift.worker is None:
        shift.worker = request.user
        shift.save()
        return redirect('bms_shifts')

    if shift.worker != request.user:
        raise Http404
    else:
        shift.worker = None
        shift.save()

        return redirect('bms_shifts')

def bms_shifts(request):
    event = get_current_event()
    shifts = BikeMutationSchedule.objects.filter(event=event).order_by('date', '-shift')

    context_dict = {
        'shifts': shifts
    }

    return render_to_response('bikemutationsignup.html',
        RequestContext(request, context_dict,))

def calendarview(request):
    # FIXME: DRY
    # campers present and meal restrictions
    event = get_current_event()

    days = list(event.days)
    campers_by_day = []
    meal_shifts_by_day = []
    bike_shifts_by_day = []
    for day in days:
        campers_by_day.append((day, User.objects.exclude(
            arrival_date__gte=day).exclude(departure_date__lt=day)))

        meal_shifts_by_day.append((day, MealShift.objects.filter(
            meal__day=day, worker__isnull=False).prefetch_related('meal')))
        bike_shifts_by_day.append((day, BikeMutationSchedule.objects.filter(
            date=day, worker__isnull=False)))

    context_dict = {
        'days': days,
        'campers_by_day': campers_by_day,
        'meal_shifts_by_day': meal_shifts_by_day,
        'bike_shifts_by_day': bike_shifts_by_day
    }
    return render_to_response('calendar.html',
        RequestContext(request, context_dict))

