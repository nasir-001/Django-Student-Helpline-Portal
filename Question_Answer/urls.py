from django.urls import path, include
from . import views 
from .views import UpdateQuestionView, DeleteQuestionView, UpdateAnswerView, DeleteAnswerView

app_name = 'Question_Answer'

urlpatterns = [
	path('index', views.index, name='index'),
	path('new_question/<int:category_id>/', views.new_question, name='new_question'),
	path('new_question/edit/<int:pk>/', UpdateQuestionView.as_view(), name='edit_question'),
	path('answer_question/edit/<int:pk>/', UpdateAnswerView.as_view(), name='edit_answer'),
	path('new_question/delete/<int:pk>/', DeleteQuestionView.as_view(), name='delete_question'),
	path('answer_question/delete/<int:pk>/', DeleteAnswerView.as_view(), name='delete_answer'),
	path('categories', views.categories, name='categories'),
	path('categories/<int:category_id>/', views.category, name='cart_questions'),	
	path('answer_question/<int:question_id>/', views.answer_question, name='answer_question'),
	path('question/<int:question_id>/', views.question, name='question'),
	path('like', views.like_question, name='like_question'),
	path('likes', views.like_answer, name='like_answer'),
	path('like', views.like_question, name='like-question'),
	path('likes', views.like_answer, name='like-answer'),

]