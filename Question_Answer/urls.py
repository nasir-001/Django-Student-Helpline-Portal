from django.urls import path, include
from . import views 

app_name = 'Question_Answer'

urlpatterns = [
	path('', include('django.contrib.auth.urls')),

	# page for all questions
	path('index', views.index, name='index'),

	# page for adding new question
	path('new_question/<int:category_id>/', views.new_question, name='new_question'),

	# page for all categories 
	path('categories', views.categories, name='categories'),

	# page for all questions and answers related to one course
	path('categories/<int:category_id>/', views.category, name='cart_questions'),	
]