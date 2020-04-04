from django.contrib import admin

# Register your models here.


from .models import Staff
from .views import staff_registration, staff_login

admin.site.register(Staff)