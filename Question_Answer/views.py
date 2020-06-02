from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib import messages
#from .forms import CategoryForm
from django.views.generic import RedirectView
from django.db.models import Q
from Helpline_Portal.models import Profile
from .forms import QuestionForm, AnswerForm
from .models import Category, Question, Answer, QuestionLike, AnswerLike
from operator import attrgetter


@login_required
def index(request):
    questions = Question.objects.order_by('-pub_date')
    context = {'questions': questions}
    return render(request, 'Question_Answer/index.html', context)


@login_required
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


@login_required
def category(request, category_id):
    category  = Category.objects.get(id=category_id)
    questions = category.question_set.order_by('-pub_date')
    context   = {'category': category, 'questions': questions}
    return render(request, 'Question_Answer/cart_questions.html', context)


@login_required
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


@login_required
def question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.order_by('-pub_date')
    context = {'question':question, 'answers': answers}
    return render(request, 'Question_Answer/question.html', context)


@login_required
def answer_question(request, question_id):
    question = Question.objects.get(id=question_id)
    category = question.category

    if request.method != 'POST':
        form = AnswerForm()

    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.owner = request.user
            new_answer.question = question
            new_answer.save()
            messages.success(request, 'Your answer to this question is posted successfully!')
            return HttpResponseRedirect(reverse('Question_Answer:index'))

    context = {'form': form, 'question': question, 'category': category}
    return render(request, 'Question_Answer/answer_question.html', context)


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


def like_question(request):
    user = request.user
    if request.method == 'POST':
        question_id = request.POST.get('question_id')
        question_obj = Question.objects.get(id=question_id)

        if user in question_obj.liked.all():
            question_obj.liked.remove(user)
        else:
            question_obj.liked.add(user)

        like, created = QuestionLike.objects.get_or_create(user=user, question_id=question_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('Question_Answer:index')


def like_answer(request):
    user = request.user
    if request.method == 'POST':
        answer_id = request.POST.get('answer_id')
        answer_obj = Answer.objects.get(id=answer_id)

        if user in answer_obj.liked.all():
            answer_obj.liked.remove(user)
        else:
            answer_obj.liked.add(user)

        like, created = AnswerLike.objects.get_or_create(user=user, answer_id=answer_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('Question_Answer:index')