from django.urls import path, include
from . import views

app_name = 'Helpline_Portal'

urlpatterns = [
    path('', views.login, name='login'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('staff_registration', views.staff_registration, name='staff_registration'),
    path('staff_index', views.staff_registration, name='staff_index'),
    path('staff_login', views.staff_login, name='staff_login'),
    path('courses', views.courses, name='courses')

]