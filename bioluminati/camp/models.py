from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

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
	(6, "Saturday"),
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

# Restrictions = (
# 	(Mammal, "Mammal"),
# 	(Onions, "Onions"),
# 	(Cilantro, "Cilantro"),
# 	(Soy, "Soy"),
# 	(Dairy, "Dairy"),
# 	(Quinoa, "Quinoa"),
# 	(Pork, "Pork"),
# 	(Olives, "Olives"),
# 	(Dairy, "Dairy"),
# 	(Peppers, "Peppers"),
# 	(Cucumber, "Cucumber"),
# 	(Nightshades, "Nightshades"),
# 	(Nuts, "Nuts")
# )


class MealShifts(models.Model):
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

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    # allow null = true and blank = true below 
    picture = models.ImageField(upload_to='profile_images', blank=True)
    city = models.CharField(max_length = 20)  
    needs_camp_bike = models.BooleanField(default=False) 
    diet_lifestyle = models.CharField(max_length = 200, choices=What_are_you, null=True, blank=True)
    meal_restrictions = models.CharField(max_length = 200, blank= True)
    other_restrictions = models.CharField(max_length=100, blank=True)
    arrival_day =  models.IntegerField(choices=Days)
    departure_day = models.IntegerField(choices=Days)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' %(
        	self.user,  self.picture, self.city, 
        	self.needs_camp_bike, 
        	self.diet_lifestyle, self.meal_restrictions, self.other_restrictions, 
        	self.arrival_day, self.departure_day
        	)

class Bikes(models.Model):
	bike_photo = models.ImageField(upload_to="bike_images", blank=True, null=True)
	bike_name = models.CharField(max_length=30)
	bike_size_inches = models.IntegerField()
	bike_owner = models.ForeignKey(User, null=True, blank=True)
	owners_last_year_on_playa = models.IntegerField()
	needs_repairs = models.BooleanField(default=False)
	in_bike_pool_this_year = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def __str__(self):
		return '%s %s %s %s %s'%(self.bike_name, self.bike_owner, self.bike_size_inches, self.needs_repairs, self.in_bike_pool_this_year)


class Tickets(models.Model):
	camper = models.ForeignKey(User)
	has_ticket = models.BooleanField(default=False)
	has_extra_ticket = models.BooleanField(default=False)
	number_of_extra_tickets = models.IntegerField(default=0)
	needs_ticket_for_self = models.BooleanField(default=False)
	needs_ticket_for_friends = models.BooleanField(default=False)
	number_of_extra_tickets_needed = models.IntegerField(default=0)
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return '%s %s %s %s'%(self.camper, self.has_ticket, self.has_extra_ticket, 
			self.number_of_extra_tickets, self.needs_ticket_for_self, self.needs_ticket_for_friends, self.number_of_extra_tickets_needed)

class BicycleMutationInventory(models.Model):
	material = models.CharField(max_length=30)
	quantity = models.IntegerField(default=0)
	units = models.CharField(max_length=30)
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return '%s %s %s'%(self.material, self.quantity, self.units)


class Inventory(models.Model):
	item = models.CharField(max_length=20, blank=True)
	needs_repairs = models.BooleanField(default=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return '%s %s'%(self.item, self.needs_repairs)


		 