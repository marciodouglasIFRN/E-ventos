from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request, 'home.html', )

#def mylogout(request):
#	logout(request)
#	return render(request, 'home.html', )