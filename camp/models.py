from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

RV = "RV"
sedan = "sedan"
small_suv = "small_suv"
large_suv = "large_suv"
x_large_suv = "x_large_suv"
small_pickup = "small_pickup"
med_pickup = "med_pickup"
large_pickup = "large_pickup"
rocket_ship = "rocket_ship"


bringing_own_tent = "bringing_own_tent"
sharing_someone_elses_tent = "sharing someone else's tent"
using_camp_yurt = "using camp yurt"
sharing_rv = "sharing rv"
other = "other"

Sleeping_arrangements = (
    (bringing_own_tent, "bringing own tent"),
    (sharing_someone_elses_tent, "sharing someone else's tent" ),
    (using_camp_yurt, "using_camp_yurt"),
    (sharing_rv, "sharing_rv"),
    (other, "other")
    )

three_feet = "three feet"
four_feet = "four feet"
five_feet = "five feet"
six_feet = "six feet"
seven_feet = "seven feet"
eight_feet = "eight feet"

one_inch = "one inch"
two_inches = "two inches"
three_inches = "three inches"
four_inches = "four inches"
five_inches = "five inches"
six_inches = "six inches"
seven_inches = "seven inches"
eight_inches = "eight inches"
nine_inches = "nine inches"
ten_inches = "ten inches"
eleven_inches = "eleven inches"



tent_size_length_feet = (
    (three_feet, "three feet"),
    (four_feet, "four feet"),
    (five_feet, "five feet"),
    (six_feet, "six feet"),
    (seven_feet, "seven feet"),
    (eight_feet, "eight feet")
    )


tent_size_length_inches = (
    (one_inch, "one inch"),
    (two_inches, "two inches"),
    (three_inches, "three inches"),
    (four_inches, "four inches"),
    (five_inches, "five inches"),
    (six_inches, "six inches"),
    (seven_inches, "seven inches"),
    (eight_inches, "eight inches"),
    (nine_inches, "nine inches"),
    (ten_inches, "ten inches"),
    (eleven_inches, "eleven inches")
    )

tent_size_width_feet = (
    (three_feet, "three feet"),
    (four_feet, "four feet"),
    (five_feet, "five feet"),
    (six_feet, "six feet"),
    (seven_feet, "seven feet"),
    (eight_feet, "eight feet")
    )


tent_size_width_inches = (
    (one_inch, "one inch"),
    (two_inches, "two inches"),
    (three_inches, "three inches"),
    (four_inches, "four inches"),
    (five_inches, "five inches"),
    (six_inches, "six inches"),
    (seven_inches, "seven inches"),
    (eight_inches, "eight inches"),
    (nine_inches, "nine inches"),
    (ten_inches, "ten inches"),
    (eleven_inches, "eleven inches")
    )

Sunday = "Sunday"
Monday = "Monday"
Tuesday = "Tuesday"
Wednesday = "Wednesday"
Thursday = "Thursday"
Friday = "Friday"
Days = (
    (0, "Sunday"),
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday")
    )

PYB_days = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday")
    )

Fish = "Fish"
Mammal = "Mammal"
Vegetarian = "Vegetarian"
Omnivore = "Omnivore"
Onions = "Onions"
Cucumber = "Cucumber"
Peppers = "Peppers"
Gluten_free = "Gluten_free"
Vegan = "Vegan"
Shellfish = "Shellfish"
Olives = "Olives"
Pork = "Pork"
Soy = "Soy"
Dairy = "Dairy"
Cilantro = "Cilantro"
Quinoa = "Quinoa"
Nightshades = "Nightshades"
Nuts = "Nuts"
Pescaterian = "Pescaterian"

What_are_you = (
    (Vegetarian, "Vegetarian"),
    (Vegan, "Vegan"),
    (Omnivore, "Omnivore"),
    (Pescaterian, "Pescaterian"),
    (Gluten_free, "Gluten_free")
)

Breakfast = "Breakfast"
Dinner = "Dinner"
Meals = (
    (Breakfast, "Breakfast"),
    (Dinner, "Dinner"),
    )

Chef = "Chef"
Sous_Chef = "Sous-Chef"
KP ="KP"
Shifts = (
    (Chef, "Chef"),
    (Sous_Chef, "Sous_Chef"),
    (KP, "KP"),
    )

Morning = "Morning"
Afternoon = "Afternoon"
PYB_shifts = (
    (Morning, "Morning"),
    (Afternoon, "Afternoon")
    )

nothing = "nothing"
needs_wheel_or_hub = "needs_wheel_or_hub"
tube = "tube"
brake_adjustment = "brake adjustment"
seat = "seat"
pedal = "pedal"
tire = "tire"
new_chain = "new_chain"
derailer = "derailer"
brake_repair = "brake repair"
head_tightening = "head tightening"
cable_repair_or_lube = "cable repair or lube"
other = "other"

Bike_repairs = (
    (nothing, "nothing"),
    (needs_wheel_or_hub, "needs_wheel_or_hub"),
    (tube, "tube"),
    (brake_adjustment, "brake adjustment"),
    (seat, "seat"),
    (pedal, "pedal"),
    (tire, "tire"),
    (new_chain, "new_chain"),
    (derailer, "derailer"),
    (brake_repair, "brake repair"),
    (head_tightening, "head tightening"),
    (cable_repair_or_lube, "cable repair or lube"),
    (other, "other")
    )


class MealShift(models.Model):
    assigned = models.BooleanField(default=False)
    day = models.IntegerField(choices=Days)
    meal = models.CharField(max_length = 10, choices=Meals)
    shift = models.CharField(max_length = 10, choices=Shifts, default=KP)
    camper = models.ForeignKey(User, null=True, blank=True, default=None)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        unique_together = ("day", "meal", "shift")

    def __str__(self):
        return '%s %s %s %s %s %s'%(self.id, self.assigned, self.day, self.meal, self.shift, self.camper)

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    city = models.CharField(max_length = 20)
    cell_number = models.CharField(max_length=15)
    email_address = models.CharField(max_length=40)
    emergency_contact_name = models.CharField(max_length=40)
    emergency_contact_phone = models.CharField(max_length=15)
    meal_restrictions = models.CharField(max_length = 200, blank= True)
    other_restrictions = models.CharField(max_length=100, blank=True)
    arrival_day =  models.IntegerField(choices=Days)
    departure_day = models.IntegerField(choices=Days)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    has_ticket = models.BooleanField(default = False)
    looking_for_ticket = models.BooleanField(default = True)
    camping_this_year = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' %(
            self.user, self.picture, self.city,
            self.cell_number, self.email_address, self.emergency_contact_name,
            self.emergency_contact_phone,
            self.meal_restrictions, self.other_restrictions,
            self.arrival_day, self.departure_day, self.has_ticket,
            self.looking_for_ticket, self.camping_this_year, self.date, self.date
            )

class Shelter(models.Model):
    user = models.OneToOneField(User)
    sleeping_arrangement = models.CharField(max_length=25, choices=Sleeping_arrangements)
    number_of_people_tent_sleeps = models.IntegerField()
    sleeping_under_ubertent = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '%s, %s, %s, %s' %(
            self.user, self.sleeping_arrangement, self.number_of_people_tent_sleeps,
            self.sleeping_under_ubertent, self.date
            )


class Vehicle(models.Model):
    user = models.OneToOneField(User)
    primary_driver_in_your_party = models.BooleanField(default=False)
    model_of_car = models.CharField(max_length=25, blank=True, default=None)
    make_of_car = models.CharField(max_length=15, blank=True, default=None)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '%s, %s, %s, %s' %(
            self.user, self.primary_driver_in_your_party, self.model_of_car,
            self.make_of_car, self.date
            )

class Bike(models.Model):
    bike_photo = models.ImageField(upload_to="bike_images", blank=True, null=True)
    bike_name = models.CharField(max_length=30)
    bike_frame_size_inches = models.IntegerField()
    bike_owner = models.ForeignKey(User, null=True, blank=True)
    owners_last_year_on_playa = models.IntegerField(default=1)
    stored_in_truck = models.BooleanField(default=True)
    needs_repairs = models.BooleanField(default=False)
    repair_needed = models.CharField(max_length=30, choices=Bike_repairs, null=True, blank=True)
    in_bike_pool_this_year = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    notes = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return '%s %s %s %s %s'%(
            self.bike_name, self.bike_owner, self.bike_size_inches,
            self.needs_repairs, self.in_bike_pool_this_year)

class BicycleMutationInventory(models.Model):
    material = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    units = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s %s %s'%(self.material, self.quantity, self.units)

class BikeMutationSchedule(models.Model):
    shift = models.CharField(max_length=25, choices=PYB_shifts)
    camper = models.ForeignKey(User, null=True, blank=True, default=None)
    day = models.IntegerField(choices = PYB_days)
    assigned = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s %s'%(self.shift, self.camper, self.day, self.assigned)

class Inventory(models.Model):
    item = models.CharField(max_length=20, blank=True)
    quantity = models.IntegerField()
    needs_repairs = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s %s'%(self.item, self.quantity, self.needs_repairs)


