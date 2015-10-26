from django.shortcuts import render
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
	# context = RequestContext(request)
	if request.method == 'POST':
		form = MealForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors 
	else:
		form = MealForm()
			
	return HttpResponse('signup.html', context_data)



# class MealView(FormView):
# 	template_name = 'signup.html'
# 	form_class = MealForm
# 	success_url = '/thanks/'

# 	def form_valid(self, form):
# 		return super(MealView, self).form_valid(form)