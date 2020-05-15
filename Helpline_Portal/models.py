from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.from .forms import RegistrationForm


class Profile(models.Model):
	user 	   = models.OneToOneField(User, on_delete=models.CASCADE)
	is_student = models.BooleanField('student status', default=False)
	is_teacher = models.BooleanField('teacher status', default=False)
	#avatar     = models.ImageField(upload_to='profile_image', null=True, blank=False)

	def __str__(self):
		return self.user.username
