from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from .models import *


class RegistrationForm(UserCreationForm):
	full_name = forms.CharField(max_length=50)
	regnumber = forms.CharField(max_length=10)
	level = forms.CharField(max_length=1)

	class Meta:
		model = User
		fields = [
			'username',
			'password1',
			'password2',
			'full_name',
			'regnumber',
			'level'
		]

	def save(self, commit=True):
					
		user = super(RegistrationForm, self).save(commit=False)
		user.full_name = self.cleaned_data.get('full_name')
		user.regnumber = self.cleaned_data.get('regnumber')
		user.level = self.cleaned_data.get('level')

		if commit:
			user.save()
			
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exits")
			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not user.is_active:
				raise forms.ValidationError("This user is not active")

		return super(LoginForm, self).clean(*args, **kwargs)	

			
			
		