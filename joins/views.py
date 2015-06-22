from django.shortcuts import render

# Create your views here.
from .forms import EmailForm, JoinForm
#this saves to database
from .models import Join

def get_ip(request):
	#ip = request.META.get("REMOTE_ADDR")
	try:
		x_forward = request.META.get("REMOTE_ADDR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("HTTP_X_FORWARDED_FOR")
	except:
	 ip = ""
	return ip
	# print ip
	# print "hello world"
import uuid
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-','').lower()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id

def home(request):
	#print request.META
 	print "this is the request"
	print request.META.get("REMOTE_ADDR")
	# print request.META.get("HTTP_X_FORWARDED_FOR")
	# print "end"
	# print request.POST
	# form = EmailForm()
	# # form = EmailForm(request.POST or None)
	# # if form.is_valid():
	# # 	email = form.cleaned_data['email']
	# # 	new_join, created = Join.objects.get_or_created(email=email)
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit = False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ref_id = get_ref_id()
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
			#redirect here
		#new_join.ip_addrees = get_ip(request)
		#new_join.ip_addrees = request.META.get("REMOTE_ADDR")
		#print new_join.ip_addrees
		#new_join.save()
		#print new_join.save()
	context = {"form": form}
	template = "home.html"
	return render(request, template, context)
