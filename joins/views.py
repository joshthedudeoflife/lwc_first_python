from django.shortcuts import render

# Create your views here.
from .forms import EmailForm, JoinForm
#this saves to database
from .models import Join

def home(request):
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_created(email=email)
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_created(email=email)
		#new_join.save()
	context = {"form": form}
	template = "home.html"
	return render(request, template, context)
