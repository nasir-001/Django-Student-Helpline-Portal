from django.urls import path, include
from . import views

app_name = 'Helpline_Portal'

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('', views.about, name='about'),

	path('accountSettings', views.accountSettings, name='accountSettings'),
    path('login', views.logins, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('staff_register', views.staff_registration, name='staff_register'),
]