from django.contrib import admin

# Register your models here.


from .models import Profile


admin.site.site_header = 'Student Helpline Portal Admin'
admin.site.register(Profile)
