from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	#return HttpResponse("about")
	return render(request, "about.html") # We've told django where to look for these templates in settings.py

def homepage(request):
	# return HttpResponse("homepage")
	return render(request, "homepage.html")


