from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answer, Category

"""
class CategoryForm(forms.ModelForm):
    title       = forms.CharField(max_length=150)
    description = forms.CharField(max_length=300)
    class Meta:
        model = Category
        fields = ['title', 'description']

"""

class QuestionForm(forms.ModelForm):
    question_title = forms.CharField(max_length=150, required=True)
    question_text  = forms.CharField(
        required=True,
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Ask your question.....',
            'rows': 10,
            'cols': 30,
        })
    )

    class Meta:
        model = Question
        fields = ['question_title', 'question_text']


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
class AnswerForm(forms.ModelForm):

    answer_text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Leave your reply...',
            'rows': 10,
            'cols': 30,
        })
    )

    class Meta:
        model = Answer
        fields = ['answer_text',]
