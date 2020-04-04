from django.db import models

# Create your models here.

class Staff(models.Model):
	username = models.CharField(max_length=50)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=50)
	phone = models.CharField(max_length=11)
	regnumber = models.CharField(max_length=11, primary_key=True)


	def __str__(self):
		return self.username