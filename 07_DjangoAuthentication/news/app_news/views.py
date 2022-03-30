from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views import View
from django.views.generic import ListView, DetailView

from .forms import NewsForm, CommentFormIsAuth, CommentFormNotIsAuth
from .models import News, Comment


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    queryset = News.objects.all()


class NewsFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'news/news_add.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            # совершаем какую-либо логику(сохраняем в базу данных)
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news/news_add')
        return render(request, 'news/news_add.html', context={'news_form': news_form})


class NewsEditFormView(View):

    def get(self, request, element_id):
        news = News.objects.get(id=element_id)
        news_form = NewsForm(instance=news)
        return render(request, 'news/news_edit.html', context={'news_form': news_form,
                                                               'element_id': element_id})

    def post(self, request, element_id):
        news = News.objects.get(id=element_id)
        news_form = NewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news.save()
        return render(request, 'news/news_edit.html', context={'news_form': news_form,
                                                               'element_id': element_id})


class NewsDetailView(DetailView):
    template_name = 'news/news_detail.html'
    model = News


class CommentFormView(View):

    def get(self, request):
        if request.user.is_authenticated:
            comment_form = CommentFormIsAuth(request.POST)
        else:
            comment_form = CommentFormNotIsAuth(request.POST)
        return render(request, 'comment/comment_add.html', context={'comment_form': comment_form})

    def post(self, request):
        if request.user.is_authenticated:
            comment_form = CommentFormIsAuth(request.POST)
        else:
            comment_form = CommentFormNotIsAuth(request.POST)

        if comment_form.is_valid():
            # совершаем какую-либо логику(сохраняем в базу данных)
            Comment.objects.create(**comment_form.cleaned_data)
            return HttpResponseRedirect('/comment/comment_add')

        return render(request, 'comment/comment_add.html', context={'comment_form': comment_form})


class LoginView(LoginView):
    template_name = 'users/login.html'


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
