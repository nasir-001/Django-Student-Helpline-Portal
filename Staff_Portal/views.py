from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponseRedirect, HttpResponse 
from Staff_Portal.forms import StaffRegForm, StaffLoginForm
from django.urls import reverse, reverse_lazy

# Create your views here.

def staff_registration(request):
	if request.method != 'POST':
		form = StaffRegForm()
	else:
		form = StaffRegForm(data=request.POST)
		if form.is_valid():
			new_staff = form.save()
			return HttpResponseRedirect(reverse('Staff_Portal:staff_login'))

	context = {
	'form':form
	}
	return render(request, 'Staff_Portal/staff_register.html', context)



def staff_login(request):
	form = StaffLoginForm(request.POST or None)

	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		staff = authenticate(username=username, password=password)
		
		return render(request, 'Staff_Portal/staff_index.html')

	context = {
	'form': form
	}
	return render(request, 'Staff_Portal/staff_login.html', context)


def staff_index(request):
	return render(request, 'Staff_Portal/staff_index.html')