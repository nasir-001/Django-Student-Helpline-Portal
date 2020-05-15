from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages
#from .forms import CategoryForm
from django.db.models import Q
from .forms import QuestionForm, AnswerForm
from .models import Category, Question, Answer
from operator import attrgetter

def index(request):
	context = {'user': request.user}
	context['categories']  = Category.objects.all() 
	context['questions']   = Question.objects.all()
	return render(request, 'Question_Answer/index.html', context)

def categories(request):
    categories = Category.objects.order_by('-pub_date')
    context    = {'categories': categories}
    
    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    categories = sorted(get_categories_queryset(query), key=attrgetter('pub_date'), reverse=True)
    context['categories'] = categories

    return render(request, 'Question_Answer/categories.html', context)


def category(request, category_id):
    category  = Category.objects.get(id=category_id)
    questions = category.question_set.order_by('-pub_date')
    context   = {'category': category, 'questions': questions}
    return render(request, 'Question_Answer/cart_questions.html', context)


def new_question(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method != 'POST':
        form = QuestionForm()
    else:
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.category = category
            new_question.owner = request.user
            new_question.save()
            messages.success(request, 'Your question is posted successfully!')
            return HttpResponseRedirect(reverse('Question_Answer:index'))

    context = {'category': category, 'form': form}
    return render(request, 'Question_Answer/new_question.html', context)


def get_categories_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        cart_lists = Category.objects.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q)
            ).distinct()
        for cart_list in cart_lists:
            queryset.append(cart_list)
    return list(set(queryset))