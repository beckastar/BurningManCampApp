from django.contrib import admin

from .models import mealShifts, UserProfile, Bikes, Tickets, Inventory, BicycleMutationInventory

admin.site.register(mealShifts)
admin.site.register(UserProfile)
admin.site.register(Bikes)
admin.site.register(Tickets)
admin.site.register(Inventory)
admin.site.register(BicycleMutationInventory)
