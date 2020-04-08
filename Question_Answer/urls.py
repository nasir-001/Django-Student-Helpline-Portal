from django.urls import path, include
from . import views

app_name = 'Question_Answer'

urlpatterns = [
	path('', include('django.contrib.auth.urls')),
	path('index', views.index, name='index'),
	
]