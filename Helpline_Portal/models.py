from django.db import models

# Create your models here.from .forms import RegistrationForm


class Users(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=15)
	full_name = models.CharField(max_length=50)
	regnumber = models.CharField(max_length=10)
	level = models.CharField(max_length=1)


	def __str__(self):
		return self.username
