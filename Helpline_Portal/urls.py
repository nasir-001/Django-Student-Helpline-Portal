from django.urls import path, include
from . import views

app_name = 'Helpline_Portal'

urlpatterns = [
    path('', views.login, name='login'),

]