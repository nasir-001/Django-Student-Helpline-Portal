from django.urls import path, include
from . import views

app_name = 'Helpline_Portal'

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

    #Staff urls
    path('staff_login', views.staff_login, name='staff_login'),
    path('staff_register', views.staff_registration, name='staff_register'),
]