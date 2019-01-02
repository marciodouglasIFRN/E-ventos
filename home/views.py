from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponse
# Create your views here.
from django.views import View


class MyHome(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home.html')

# def home(request):
#
# 	return render(request, 'home.html')

# def home(request):
# 	return render(request,'home.html')
# @login_required


def about(request):
	data = {}
	data['usuario'] = request.user
	return render(request, 'about.html', data )

#def mylogout(request):
#	logout(request)
#	return render(request, 'home.html', )