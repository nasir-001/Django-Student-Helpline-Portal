from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.http import HttpResponseRedirect, HttpResponse


def index(request):
	context = {}
	return render(request, 'Question_Answer/index.html', context)

	