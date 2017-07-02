from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Meal, MealShift, MealRestriction, User, UserAttendance, Bike, Inventory, BicycleMutationInventory, BikeMutationSchedule, Vehicle

class UserAttendanceAdmin(admin.ModelAdmin):
    list_filter = ('event', 'camping_this_year',
        'paid_dues', 'has_ticket', 'looking_for_ticket')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')

admin.site.register(Meal)
admin.site.register(MealShift)
admin.site.register(User, UserAdmin)
admin.site.register(UserAttendance, UserAttendanceAdmin)
admin.site.register(Bike)
admin.site.register(Inventory)
admin.site.register(BicycleMutationInventory)
admin.site.register(MealRestriction)
admin.site.register(BikeMutationSchedule)
admin.site.register(Vehicle)
