from django.contrib import admin

# Register your models here.

from .models import Users
from .views import register
admin.site.register(Users)

