from django.contrib import admin
from .models import Category, Question, Answer, QuestionLike, AnswerLike
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



class QuestionLikeAdmin(admin.ModelAdmin):
	class Meta:
		QuestionLike



class AnswerLikeAdmin(admin.ModelAdmin):
	class Meta:
		AnswerLike

admin.site.site_header = 'Admin Student Helpline Portal'
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuestionLike, QuestionLikeAdmin)
admin.site.register(AnswerLike, AnswerLikeAdmin)