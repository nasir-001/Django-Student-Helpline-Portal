from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def login(request):
	return render(request, 'Helpline_Portal/login.html')