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
from django.contrib.auth.views import login, logout
from camp import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    # FIXME: should the public be able to register?
    #  Likely should have a prompt to contact council or seek sponsor
    #  url(r'^register/', views.register, name='register'),
    url(r'^login/', login, name='login',kwargs={'template_name': 'login.html'}),
    url(r'^logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^confirm/', views.register, name='confirm'),
    url(r'^about/', views.about, name='about'),
    url(r'^prep/', views.prep, name='prep'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^vehicle/', views.vehicle, name='vehicle'),
    url(r'^shelter/', views.shelter, name='shelter'),

    # chef signup
    url(r'^meal_shifts/$', views.meal_shifts, name='meal_shifts'),
    url(r'^chef_signup/(?P<meal_id>[^/]+)/$', views.chef_signup, name='chef_signup'),
    url(r'^chef_requirements/(?P<meal_id>[^/]+)/$', views.chef_requirements, name='chef_requirements'),
    url(r'^worker_signup/(?P<shift_id>[^/]+)/$', views.worker_signup, name='worker_signup'),
    url(r'^bikes/$', views.show_bike_form, name='bikes'),
    url(r'^bikes/(?P<bike_id>[^/]+)/edit/$', views.edit_bike, name='edit_bike'),
    url(r'^remove-bike-from-db/', views.remove_bike, name='remove_bike'),

    url(r'^meal_schedule/', views.meal_schedule, name="meal_schedule"),
    url(r'^inventory/', views.show_inventory_form, name="inventory"),
    url(r'^remove_items_from_truck/', views.remove_items_from_truck, name="remove_inventory"),
    url(r'^edit_inventory_item/', views.edit_truck_inventory, name="edit_inventory"),
    url(r'^campers/', views.campers, name="campers"),
    url(r'^calendar/', views.calendarview, name="calendar"),
    url(r'^bikemutation/shifts/$', views.bms_shifts, name="bms_shifts"),
    url(r'^bikemutation/shifts/(?P<shift_id>[^/]+)/$', views.bms_worker_signup, name="bms_worker_signup"),

    url(r'^remove_items_from_bikemutation/', views.remove_items_from_bikemutation, name="remove_items_from_bikemutation"),#change this
    url(r'^edit_bikemutation_item/', views.edit_bikemutation, name="edit_bikemutation"),    #change this
    url(r'^bikemutation/schedule/$', views.bikemutation, name='bikemutation'),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^export/', views.export, name='export'),
]
