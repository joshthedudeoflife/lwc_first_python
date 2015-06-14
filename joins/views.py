from django.shortcuts import render

# Create your views here.
from .forms import EmailForm, JoinForm
#this saves to database
from .models import Join

def get_ip(request):
	try:
		#print "hello world"
		x_forward = request.META.get("REMOTE_ADDR")
	# 	if x_forward:
	# 		ip = x_forward.split(",")[0]
	# 	else:
	# 		ip = request.META.get("REMOTE_ADDR")
	except:
	 ip = ""
	return x_forward
	print "hello world"

def home(request):
	#print request.META.get("REMOTE_ADDR")
	# print request.POST
	# form = EmailForm()
	# # form = EmailForm(request.POST or None)
	# # if form.is_valid():
	# # 	email = form.cleaned_data['email']
	# # 	new_join, created = Join.objects.get_or_created(email=email)
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		#email = form.cleaned_data['email']
		#new_join_old, created = Join.objects.get_or_create(email=email)
		new_join.ip_addrees = get_ip(request)
		new_join.save()
	context = {"form": form}
	template = "home.html"
	return render(request, template, context)
