from django.contrib import admin
<<<<<<< HEAD
from .models import Category, Question, Answer, QuestionLike, AnswerLike
=======
from .models import Category, Question, Answer, Like
>>>>>>> d999ee1f1e4a9bfd794debd8d578bb3b75a6b3ae
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


<<<<<<< HEAD

class QuestionLikeAdmin(admin.ModelAdmin):
	class Meta:
		QuestionLike



class AnswerLikeAdmin(admin.ModelAdmin):
	class Meta:
		AnswerLike
=======
class LikeAdmin(admin.ModelAdmin):
	class Meta:
		Like
>>>>>>> d999ee1f1e4a9bfd794debd8d578bb3b75a6b3ae

admin.site.site_header = 'Admin Student Helpline Portal'
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
<<<<<<< HEAD
admin.site.register(QuestionLike, QuestionLikeAdmin)
admin.site.register(AnswerLike, AnswerLikeAdmin)
=======
admin.site.register(Like, LikeAdmin)
>>>>>>> d999ee1f1e4a9bfd794debd8d578bb3b75a6b3ae
