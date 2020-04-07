from django.contrib import admin

# Register your models here.

from .models import Users
from .forms import RegistrationForm

admin.site.register(Users)
