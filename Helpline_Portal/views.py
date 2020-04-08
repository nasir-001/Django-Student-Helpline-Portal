from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponseRedirect, HttpResponse 
from Helpline_Portal.forms import RegistrationForm, LoginForm, StaffRegForm, StaffLoginForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return render(request, 'Question_Answer/index.html')
	

	context = {'form': form}
	return render(request, 'Helpline_Portal/login.html', context)

@login_required
def register(request):
	if request.method != 'POST':
		form = RegistrationForm()
	else:
		form = RegistrationForm(data=request.POST)
		if form.is_valid():
			form = form.save()

			return HttpResponseRedirect(reverse('Helpline_Portal:login'))

	context = {
		'form': form
	}
	return render(request, 'Helpline_Portal/register.html', context)

@login_required
def logout(request):
	return render(request, 'Helpline_Portal/logout.html')


def staff_registration(request):
	if request.method != 'POST':
		form = StaffRegForm()
	else:
		form = StaffRegForm(data=request.POST)
		if form.is_valid():
			new_staff = form.save()
			return HttpResponseRedirect(reverse('Helpline_Portal:staff_login'))

	context = {
	'form':form
	}
	return render(request, 'Helpline_Portal/staff_register.html', context)



def staff_login(request):
	form = StaffLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		staff = authenticate(username=username, password=password)
		
		return render(request, 'Question_Answer/index.html')

	context = {
	'form': form
	}
	return render(request, 'Helpline_Portal/staff_login.html', context)
