from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponseRedirect, HttpResponse 
from Helpline_Portal.forms import RegistrationForm, LoginForm
# Create your views here.

def login(request):
	form = LoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return render(request, 'Helpline_Portal/index.html')
	

	context = {'form': form}
	return render(request, 'Helpline_Portal/login.html', context)


def register(request):
	if request.method != 'POST':
		form = RegistrationForm()
	else:
		form = RegistrationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()

			return redirect('Helpline_Portal:login')

	context = {
		'form': form
	}
	return render(request, 'Helpline_Portal/register.html', context)
