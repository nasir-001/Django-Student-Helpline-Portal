from django.urls import path, include
from . import views

app_name = 'Helpline_Portal'

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
    path('', views.login, name='login'),
    path('index', views.login, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]