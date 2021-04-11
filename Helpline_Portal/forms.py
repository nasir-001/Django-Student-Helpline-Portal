from django import forms
from django.db import transaction
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, PasswordInput, EmailInput



# class StudentForm(UserCreationForm):
# 	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
# 	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))

# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'first_name', 'password1', 'password2')
# 		widgets = {
# 			'username': TextInput(attrs={'placeholder': 'username'}),
# 			'email': EmailInput(attrs={'placeholder': 'email'}),
# 			'first_name': TextInput(attrs={'placeholder': 'full name'}),
# 		}


# 		def clean_email(self):
# 			email = self.cleaned_data.get('email')

# 			try:
# 				User.objects.get(email=email)
# 			except ObjectDoesNotExist:
# 				return email
# 			else:
# 				raise forms.ValidationError('This email is not availbale!')

# 		def clean_last_name(self):
# 			email = self.cleaned_data.get('last_name')

# 			try:
# 				User.objects.get(last_name=last_name)
# 			except ObjectDoesNotExist:
# 				return last_name
# 			else:
# 				raise forms.ValidationError('User with this regnumber already exists!')



# class TeacherForm(UserCreationForm):
# 	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
# 	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))
	
# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
# 		widgets = {
# 			'username': TextInput(attrs={'placeholder': 'username'}),
# 			'email': EmailInput(attrs={'placeholder': 'email'}),
# 			'first_name': TextInput(attrs={'placeholder': 'first name'}),
# 			'last_name': TextInput(attrs={'placeholder': 'last name'}),
# 		}
		
# 		def clean_email(self):
# 			email = self.cleaned_data.get('email')

# 			try:
# 				User.objects.get(email=email)
# 			except ObjectDoesNotExist:
# 				return email
# 			else:
# 				raise forms.ValidationError('This email is not availbale!')



class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['avatar',]
        


class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')

		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("This user does not exits")

		return super(LoginForm, self).clean(*args, **kwargs)