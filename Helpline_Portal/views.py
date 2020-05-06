from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages 
from Helpline_Portal.forms import *
from django.urls import reverse
# Create your views here.

def logins(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		messages.success(request, 'You have login successfuly')
		return HttpResponseRedirect(reverse('Question_Answer:index'))
	
	context = {'form': form}
	return render(request, 'Helpline_Portal/login.html', context)

def register(request):
	if request.method != 'POST':
		form = RegistrationForm()
	else:
		form = RegistrationForm(data=request.POST)
		if form.is_valid():
			form = form.save()
			messages.success(request, 'Registration successful')
			return HttpResponseRedirect(reverse('Helpline_Portal:login'))

	context = {
		'form': form
	}
	return render(request, 'Helpline_Portal/register.html', context)


def logout(request):
	return render(request, 'Helpline_Portal/logout.html')


def staff_registration(request):
	if request.method != 'POST':
		form = StaffRegForm()
	else:
		form = StaffRegForm(data=request.POST)
		if form.is_valid():
			new_staff = form.save()
			messages.sucess(request, 'Registration successful')
			return HttpResponseRedirect(reverse('Helpline_Portal:login'))

	context = {
	'form':form
	}
	return render(request, 'Helpline_Portal/staff_register.html', context)


def about(request):
	return render(request, 'Helpline_Portal/about.html')