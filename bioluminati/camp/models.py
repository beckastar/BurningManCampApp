from django.db import models
from django.forms import ModelForm
# is above line in the correct file?

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
	camper = models.CharField(max_length = 30, default="none")

	class Meta:
		unique_together = ("day", "meal", "shift")

	def __str__(self):
		return '%s %s %s %s'%(self.day, self.meal, self.shift, self.camper)

		 