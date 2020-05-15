from django import forms
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class StudentForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

		@transaction.atomic
		def save(self, commit=True):
			user = super().save(commit=False)
			user.email = self.cleaned_data.get('email')
			user.first_name = self.cleaned_data.get('first_name')
			user.last_name  = self.cleaned_data.get('last_name')

			if commit:
				user.save()
			return user


class TeacherForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
		
		def clean_email(self):
			email = self.cleaned_data.get('email')

			try:
				User.objects.get(email=email)
			except ObjectDoesNotExist:
				return email
			else:
				raise forms.ValidationError('This email is not availbale!')


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

		return super(LoginForm, self).clean(*args, **kwargs)	


