from django.contrib import admin
from .models import Category, Question, Answer
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

admin.site.site_header = 'Admin Student Helpline Portal'
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)