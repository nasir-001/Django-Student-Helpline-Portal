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
		fields = ('username', 'password1', 'password2', 'full_name', 'regnumber', 'level')

		
		def clean_username(self):
			username = self.cleaned_data['username']
			try:
				User.objects.get('username')
			except ObjectDoesNotExist:
				return username
			else:
				raise forms.ValidationError('Username is already in use.')

		def clean_email(self):
			email = self.cleaned_data['email']
			try:
				User.objects.get(email=email)
			except ObjectDoesNotExist:
				return email
			else:
				raise forms.ValidationError('Email is already in use.')

"""
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['full_name'].widget = forms.TextInput(attrs={'required': True})
		self.fields['regnumber_name'].widget = forms.TextInput(attrs={'required': True})
		self.fields['level'].widget = forms.TextInput(attrs={'required': True})
"""
	
			
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

			
			
class StaffRegForm(UserCreationForm):
	email = forms.EmailField(max_length=50, required=True)
	regnumber = forms.CharField(max_length=10)
	phone = forms.CharField(max_length=11, required=True)


	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email', 'regnumber', 'phone')


	def save(self, commit=True):
		staff = super(StaffRegForm, self).save(commit=False)
		staff.regnumber = self.cleaned_data.get('regnumber')
		staff.phone = self.cleaned_data.get('phone')

		if commit:
			staff.save()

	def check_password(self):
		if password1 != password2:
			raise forms.ValidationError("password didn't match.")

class StaffLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			staff = authenticate(username=username, password=password)
			if not staff:
				raise forms.ValidationError("This user does not exits")
			if not staff.check_password(password):
				raise forms.ValidationError("Incorrect password")
			if not staff.is_active:
				raise forms.ValidationError("This user is not active")

		return super(StaffLoginForm, self).clean(*args, **kwargs)			