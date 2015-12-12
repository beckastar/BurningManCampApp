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
from camp.views import index, meal_schedule, signup_for_shift, remove_self_from_shift, profile, register, show_bike_form, remove_bike, edit_bike, bikemutation, inventory, about
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^signup/$', signup_for_shift, name='signup'),
    url(r'^remove-self-from-shift/$', remove_self_from_shift, name="remove_self_from_shift"),
    url(r'^accounts/profile/$', profile, name='profile'),
    url(r'^login/', 'django.contrib.auth.views.login', name='foo',kwargs={'template_name': 'login.html'}),
    url(r'^/logout/$', 'django.contrib.auth.views.logout', name='logout', kwargs={'next_page': '/'}),
    url(r'^register/', register, name='register'),
    url(r'^confirm/', register, name='confirm'),  
    url(r'^bikes/', show_bike_form, name='bikes'),
    url(r'^remove-bike-from-db/', remove_bike, name='remove_bike'),
    url(r'^edit_bike/', edit_bike, name='edit_bike'),
    url(r'^bikemutation/$', bikemutation, name='bikemutation'), 
    url(r'^about/', about, name='about'), 
    url(r'^meal_schedule/', meal_schedule, name="meal_schedule")
    # url(r'^accounts/', include('django.contrib.auth.urls')),
]
