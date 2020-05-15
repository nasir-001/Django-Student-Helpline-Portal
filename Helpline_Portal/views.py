from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages 
from .forms import StudentForm, TeacherForm, LoginForm
from django.urls import reverse
from django.db import transaction
from .models import Profile
from django.template import RequestContext
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

	if request.method == 'POST':
		form = StudentForm(request.POST)

		if form.is_valid():
			user = form.save()
			user.profile = Profile.objects.create(is_student=True, user=user)
			
			return HttpResponseRedirect(reverse('Helpline_Portal:login'))
	else:
		form = StudentForm()
	
	context = {'form': form}
	return render(request, 'Helpline_Portal/register.html', context)


def staff_registration(request):

	if request.method == 'POST':
		form = TeacherForm(request.POST)

		if form.is_valid():	
			
			user = form.save()
			user.profile = Profile.objects.create(is_teacher=True, user=user)
			
			return HttpResponseRedirect(reverse('Helpline_Portal:login'))
	else:
		form = TeacherForm()	
	
	context = {'form': form}
	return render(request, 'Helpline_Portal/register.html', context)


def logout(request):
	return render(request, 'Helpline_Portal/logout.html')


def about(request):
	return render(request, 'Helpline_Portal/about.html')
