from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404, HttpResponse
from .models import Task
from .forms import TaskForm, ArticleForm
from .forms import NameForm
from .models import Article
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import DetailView


def index(request):
    form = NameForm()
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks}, {'form': form})


def about(request):
    form = NameForm()
    latest_articles_list = Article.objects.order_by('-pub_date')[:10]
    return render(request, 'main/about.html', {'latest_articles_list': latest_articles_list}, {'form': form})


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'main/detail.html', {'article': a, 'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('detail', args=(a.id,)))


def test(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/test.html', context, {'form': form})


def vvod(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('about')

    form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'main/vvod.html', context, {'form': form})


def notes(request):
    form = NameForm()
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/notes.html', {'title': 'Заметки', 'tasks': tasks}, {'form': form})


def user(DetailView):
    form = NameForm()
    model = User
    return render(DetailView, 'main/user.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/user_login.html', {'form': form})


def dashboard(request):
    return render(request, 'main/dashboard.html', {'section': 'dashboard'})


def str(request):
    return render(request, 'main/str.html', {'section': 'str'})
