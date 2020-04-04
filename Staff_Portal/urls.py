from django.urls import path, include
from . import views

app_name = 'Staff_Portal'

urlpatterns = [
	path('', views.staff_login, name='staff_login'),
    path('staff_register', views.staff_registration, name='staff_register'),
    path('staff_index', views.staff_index, name='staff_index'),
    

]