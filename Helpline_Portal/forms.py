from django import forms
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm



class StudentForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'password1', 'password2')

		def clean_email(self):
			email = self.cleaned_data.get('email')

			try:
				User.objects.get(email=email)
			except ObjectDoesNotExist:
				return email
			else:
				raise forms.ValidationError('This email is not availbale!')

		def clean_last_name(self):
			email = self.cleaned_data.get('last_name')

			try:
				User.objects.get(last_name=last_name)
			except ObjectDoesNotExist:
				return last_name
			else:
				raise forms.ValidationError('User with this regnumber already exists!')



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



class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar',]
        


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


