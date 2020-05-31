from django.contrib import admin
from .models import Category, Question, Answer, Like
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
	class Meta:
		model = Question


class AnswerAdmin(admin.ModelAdmin):
	class Meta:
		model = Answer


class CategoryAdmin(admin.ModelAdmin):
	class Meta:
		Category


class LikeAdmin(admin.ModelAdmin):
	class Meta:
		Like

admin.site.site_header = 'Admin Student Helpline Portal'
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Like, LikeAdmin)