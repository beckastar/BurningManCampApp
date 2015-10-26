from django.db import models
from django.forms import ModelForm
# is above line in the correct file?

class mealShifts(models.Model):
	Sunday = "Sunday"
	Monday="Monday"
	Tuesday = "Tuesday"
	Wednesday = "Wednesday"
	Thursday = "Thursday"
	Friday = "Friday"
	Days_with_meals = (
		(Sunday, "Sunday"),
		(Monday, "Monday"),
		(Tuesday, "Tuesday"),
		(Wednesday, "Wednesday"),
		(Thursday, "Thursday"),
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
	day = models.CharField(max_length = 7, choices=Days_with_meals, default=Sunday)
	meal = models.CharField(max_length = 10, choices=Meals, default=Breakfast)
	shift = models.CharField(max_length = 10, choices=Shifts, default=KP)
	camper = models.CharField(max_length = 30, default="none")

	def __str__(self):
		return self.day