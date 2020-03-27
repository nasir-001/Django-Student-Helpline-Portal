from django.contrib import admin

# Register your models here.

from .models import Users, Staff
from .views import register, staff_registration
admin.site.register(Users)
admin.site.register(Staff)

