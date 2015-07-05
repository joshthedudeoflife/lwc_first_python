from django.shortcuts import render

def testhome(request):
	context = {}
	template = "donotuse.html"
	return render(request, template, context)
# def home(request):
# 	context = {}
# 	template = "home.html"
# 	return render(request, template, context)

# def home(request):
# 	context = {}
# 	template = "home.html"
# 	return render(request, template, context)
