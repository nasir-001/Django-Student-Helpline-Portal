from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model
from .models import *


class StaffRegForm(UserCreationForm):
	regnumber = forms.CharField(max_length=10)
	phone = forms.CharField(max_length=11, required=True)


	class Meta:
		model = User
		fields = [
			'username',
			'password1',
			'password2',
			'email',
			'regnumber',
			'phone'
		]



	def save(self, commit=True):
		staff = super(StaffRegForm, self).save(commit=False)
		staff.regnumber = self.cleaned_data.get('regnumber')
		staff.phone = self.cleaned_data.get('phone')

		if commit:
			staff.save()

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