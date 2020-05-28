from django.contrib import admin

# Register your models here.


from .models import Profile


admin.site.site_header = 'Admin Student Helpline Portal'
admin.site.register(Profile)
