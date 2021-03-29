from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import StudentForm, TeacherForm, LoginForm, ProfileForm
from django.urls import reverse
from django.db import transaction
from .models import Profile
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


@login_required
def accountSettings(request):
	profile = request.user.profile 
	if request.user.profile.is_teacher:
		form = TeacherForm(request.POST, instance=request.user)
		profile_form = ProfileForm(instance=profile)

		if request.method == 'POST':
			form = TeacherForm(request.POST, instance=request.user)
			profile_form = ProfileForm(request.POST, request.FILES or None, instance=request.user.profile)

			if form.is_valid() and profile_form.is_valid():
				user = form.save()
				avatar = profile_form.save(commit=False)
				avatar.save()
				
				login(request, user)

				messages.success(request, 'Your account has been updated successfuly!')
				return HttpResponseRedirect(reverse('Question_Answer:index'))
		else:
			form = TeacherForm(instance=request.user)
			profile_form = ProfileForm(instance=request.user.profile)

	else:
		form = StudentForm(request.POST, instance=request.user)
		profile_form = ProfileForm(instance=profile)

		if request.method == 'POST':
			form = StudentForm(request.POST, instance=request.user)
			profile_form = ProfileForm(request.POST, request.FILES or None, instance=request.user.profile)

			if form.is_valid() and profile_form.is_valid():
				user = form.save()
				avatar = profile_form.save(commit=False)
				avatar.save()

				login(request, user)

				messages.success(request, 'Your account has been updated successfuly!')
				return HttpResponseRedirect(reverse('Question_Answer:index'))
		else:
			form = StudentForm(instance=request.user)
			profile_form = ProfileForm(instance=request.user.profile)

	context = {'form': form,'profile_form': profile_form}
	return render(request, 'Helpline_Portal/accountSettings.html', context)


# def register(request):

# 	if request.method == 'POST':
# 		form = StudentForm(request.POST)

# 		if form.is_valid():
# 			user = form.save()
# 			user.profile = Profile.objects.create(is_student=True, user=user)

# 			return HttpResponseRedirect(reverse('Helpline_Portal:login'))
# 	else:
# 		form = StudentForm()

# 	context = {'form': form}
# 	return render(request, 'Helpline_Portal/register.html', context)


# def staff_registration(request):

# 	if request.method == 'POST':
# 		form = TeacherForm(request.POST)

# 		if form.is_valid():	
			
# 			user = form.save()

# 			user.profile = Profile.objects.create(is_teacher=True, user=user)
			
# 			return HttpResponseRedirect(reverse('Helpline_Portal:login'))
# 	else:
# 		form = TeacherForm()
	
# 	context = {'form': form}
# 	return render(request, 'Helpline_Portal/staff_registration.html', context)


def logouts(request):
	logout(request)
	return render(request, 'Helpline_Portal/logout.html')


def about(request):
	return render(request, 'Helpline_Portal/about.html')


def handler404(request, exception):
	return render(request, 'Helpline_Portal/404.html', status=404)


def handler500(request):
	return render(request, 'Helpline_Portal/500.html', status=500)