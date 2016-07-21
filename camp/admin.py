from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Meal, MealShift, User, Bike, Inventory, BicycleMutationInventory, BikeMutationSchedule, Vehicle

admin.site.register(Meal)
admin.site.register(MealShift)
admin.site.register(User, UserAdmin)
admin.site.register(Bike)
admin.site.register(Inventory)
admin.site.register(BicycleMutationInventory)
admin.site.register(BikeMutationSchedule)
admin.site.register(Vehicle)
