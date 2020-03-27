from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponseRedirect, HttpResponse 
from Helpline_Portal.forms import RegistrationForm, LoginForm, StaffRegForm, StaffLoginForm

# Create your views here.

def login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request)
		
		return render(request, 'Helpline_Portal/index.html')
	context = {'form': form}
	return render(request, 'Helpline_Portal/login.html', context)



def index(request):
	return render(request, 'Helpline_Portal/index.html')


def register(request):
	if request.method != 'POST':
		form = RegistrationForm()
	else:
		form = RegistrationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()

			login(request)
			return redirect('Helpline_Portal:index')

	context = {
		'form': form
	}
	return render(request, 'Helpline_Portal/register.html', context)


def staff_registration(request):
	if request.method != 'POST':
		form = StaffRegForm()
	else:
		form = StaffRegForm(data=request.POST)
			
		if form.is_valid():
			new_staff = form.save()
			
			login(request)		
			return redirect('Helpline_Portal:courses')

	context = {'form':form}
	return render(request, 'Helpline_Portal/staff_registration.html', context)

def staff_login(request):
	form = StaffLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		staff = authenticate(username=username, password=password)
		
		login(request)
		return render(request, 'Helpline_Portal/staff_index.html')

	context = {'form': form}
	return render(request, 'Helpline_Portal/staff_login.html', context)


def courses(request):
	return render(request, 'Helpline_Portal/courses.html')