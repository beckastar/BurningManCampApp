from django.shortcuts import render
from django.http import HttpResponse
from models import mealShifts
from django.shortcuts import render_to_response, get_object_or_404
from forms import MealForm
from django.core.context_processors import csrf 
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

def index(request):
	shifts = mealShifts.objects.all()
	return render(request, "index.html", {'shifts':shifts})

def login(request):
    return render(request, 'login.html')

@login_required
def profile(request):
	return render(request, "profile.html")

# @login_required(login_url='login.html')
def signup(request):
	shifts = mealShifts.objects.all()
	username = None
	if request.user.is_authenticated():
		username = request.user.get_username()
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
			
	return render_to_response('signup.html', RequestContext(request, {'form':form,'shifts':shifts, 'username':username},))

# def register(request):
#     if request.method == 'POST':
#         uf = UserForm(request.POST, prefix='user')
#         upf = UserProfileForm(request.POST, prefix='userprofile')
#         if uf.is_valid() * upf.is_valid():
#             user = uf.save()
#             userprofile = upf.save(commit=False)
#             userprofile.user = user
#             userprofile.save()
#             return django.http.HttpResponseRedirect('registration_complete.html')
#     else:
#         uf = UserForm(prefix='user')
#         upf = UserProfileForm(prefix='userprofile')
#     return django.shortcuts.render_to_response('register.html', 
#                                                dict(userform=uf,
#                                                     userprofileform=upf),
#                                                context_instance=django.template.RequestContext(request))


