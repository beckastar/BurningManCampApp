from django.shortcuts import render
from django.http import HttpResponse
from models import mealShifts
from django.shortcuts import render_to_response, get_object_or_404
from forms import MealForm
from django.core.context_processors import csrf 
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

def index(request):
	shifts = mealShifts.objects.all()
	return render(request, "index.html", {'shifts':shifts})

def signup(request):
	shifts = mealShifts.objects.all()
	# context = RequestContext(request)
	if request.method == 'POST':
		form = MealForm(request.POST)
		if form.is_valid():
			form.save()
			return index(request)
		# else:
		# 	print form.errors 
	else:
		form = MealForm()
			
	return render_to_response('signup.html', RequestContext(request, {'form':form,'shifts':shifts},))


