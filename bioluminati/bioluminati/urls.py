"""bioluminati URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from camp.views import index, login, remove_items_from_truck, about, prep, campers, signup_for_shift, meal_schedule, remove_self_from_shift, show_signup_table, profile, vehicle, shelter, remove_bike, edit_bike, show_bike_form, bikemutation, edit_truck_inventory, show_inventory_form, register, remove_self_from_pyb_shift, signup_for_pyb_shift, show_pybsignup, calendarview, edit_bikemutation, remove_items_from_bikemutation

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^register/', register, name='register'),
    url(r'^login/', 'django.contrib.auth.views.login', name='foo',kwargs={'template_name': 'login.html'}),
    url(r'^/logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    url(r'^confirm/', register, name='confirm'),  
    url(r'^about/', about, name='about'), 
    url(r'^prep/', prep, name='prep'), 
    url(r'^profile/', profile, name='profile'), 
    url(r'^vehicle/', vehicle, name='vehicle'),
    url(r'^shelter/', shelter, name='shelter'),
    url(r'^signup/$', signup_for_shift, name='signup'),
    url(r'^remove-self-from-shift/$', remove_self_from_shift, name="remove_self_from_shift"),
    url(r'^bikes/', show_bike_form, name='bikes'),
    url(r'^remove-bike-from-db/', remove_bike, name='remove_bike'),
    url(r'^edit_bike/', edit_bike, name='edit_bike'),
    url(r'^meal_schedule/', meal_schedule, name="meal_schedule"),
    url(r'^inventory/', show_inventory_form, name="inventory"),
    url(r'^remove_items_from_truck/', remove_items_from_truck, name="remove_inventory"),
    url(r'^edit_inventory_item/', edit_truck_inventory, name="edit_inventory"),    
    url(r'^campers/',campers, name="campers"),
    url(r'^calendar/', calendarview, name="calendar"),
    url(r'^bikemutation/$', bikemutation, name='bikemutation'),  
    url(r'^remove_items_from_bikemutation/', remove_items_from_bikemutation, name="remove_items_from_bikemutation"),#change this
    url(r'^edit_bikemutation_item/', edit_bikemutation, name="edit_bikemutation"),    #change this 
    url(r'^remove-self-from-pyb-shift/', remove_self_from_pyb_shift, name="remove_self_from_pyb_shift"),
    url(r'^signup_for_pyb_shift/', signup_for_pyb_shift, name="signup_for_pyb_shift"),
    url(r'^bikemutationsignup/', show_pybsignup, name="show_pybsignup")
    # url(r'^accounts/', include('django.contrib.auth.urls')),
]
