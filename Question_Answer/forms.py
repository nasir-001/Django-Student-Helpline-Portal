from django import forms

from .models import Question, Answer, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description']


class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'placeholder': 'Leave your reply...',
            'rows': 4,
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
            'rows': 4,
        })
    )

    class Meta:
        model = Answer
        fields = ['answer_text',]


