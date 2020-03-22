from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



def login(request):
	return render(request, 'Helpline_Portal/login.html')



def index(request):
	return render(request, 'Helpline_Portal/index.html')


def signup(request):
	return render(request, 'Helpline_Portal/signup.html')