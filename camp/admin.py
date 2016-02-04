from django.contrib import admin

from .models import MealShift, UserProfile, Bike, Inventory, BicycleMutationInventory, BikeMutationSchedule, Vehicle

admin.site.register(MealShift)
admin.site.register(UserProfile)
admin.site.register(Bike)
admin.site.register(Inventory)
admin.site.register(BicycleMutationInventory)
admin.site.register(BikeMutationSchedule)
admin.site.register(Vehicle)
