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
    return render(request, "profile.html", RequestContext(request, {'form': form, 'profile': profile, },))

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

# this needs to work 
def remove_self_from_shift(request):
    print "REMOVE CALLED!"
    if request.method == 'POST':
        shift_id = int(request.POST.get('shift_id'))
        print "CALLED WITH SHIFT ID=%s" % shift_id

        shift = MealShifts.objects.get(id=shift_id)
        # print "Shift to remove: %s" % shift
        # print "shift.camper = %s" % shift.camper
        # print "request.user = %s" % request.user
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

 
def bike_form(request):
    model = Bikes
    bicycles = Bikes.objects.all()
    form = BikeForm(data = request.POST)
    if request.method == "POST":

        if form.is_valid():
            form.save(commit=False)
            import pdb; pdb.set_trace()

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


# i tried to allow users to edit the inventory table 
# def inventory(request, id):
#     model = Inventory
#     # thing = Inventory.objects.get(pk=id) 
#     if request.method == "POST":
#         stuff = Inventory.objects.get(id=id)
#         form = InventoryForm(data = request.POST, instance=stuff) 
#         if form.is_valid():
#             # if Inventory.filter(item='item').exists()
#             # obj = form.save(commit=False)
#             form.save()

#     else:
#         stuff = Inventory.objects.get(id=id)
#         form = InventoryForm(instance=stuff)
#     context = RequestContext(request)
#     return render_to_response('inventory.html', {
#             'form':form, 'stuff':stuff
#             }, RequestContext(request))



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


