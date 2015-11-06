from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class mealShifts(models.Model):
	Sunday = "Sunday"
	Monday = "Monday"
	Tuesday = "Tuesday"
	Wednesday = "Wednesday"
	Thursday = "Thursday"
	Friday = "Friday"
	Days = (
		(Sunday, "Sunday"),
		(Monday, "Monday"),
		(Tuesday, "Tuesday"),
		(Wednesday, "Wednesday"),
		(Thursday, "Thursday"),
		(Friday, "Friday"),
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
	assigned = models.BooleanField(default=False)
	day = models.CharField(max_length = 10, choices=Days, default=Sunday)
	meal = models.CharField(max_length = 10, choices=Meals, default=Dinner)
	shift = models.CharField(max_length = 10, choices=Shifts, default=KP)
	camper = models.OneToOneField(User)

	class Meta:
		unique_together = ("day", "meal", "shift")

	def __str__(self):
		return '%s %s %s %s'%(self.day, self.meal, self.shift, self.camper)

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    playa_name = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    city = models.CharField(max_length = 20)
    number_of_burns = models.IntegerField()
    years_with_bio = models.IntegerField(default=0)
    petronus = models.CharField(max_length=20, blank=True)
    needs_camp_bike = models.BooleanField(default=False)
    twitter_handle = models.CharField(max_length=30)
    facebook_name = models.CharField(max_length=30)
    favorite_nonfiction = models.CharField(max_length=50)
    favorite_fiction = models.CharField(max_length=50)
    favorite_movie = models.CharField(max_length=50)
    playa_hope = models.CharField(max_length=25)
    playa_fear = models.CharField(max_length=25)

    def __str__(self):
        return '%s %s %s %s'%(self.website, self.picture, self.shift, self.camper)

class Bikes(models.Model):
	bike_name = models.CharField(max_length=30)
	# bike_owner = models.OneToOneField(User)
	# user_on_playa = models.OneToOneField(User)
	needs_repairs = models.BooleanField(default=False) 

	def __str__(self):
		return '%s %s %s %s'%(self.bike_name, self.bike_owner, self.user_on_playa, self.needs_repairs)




		 