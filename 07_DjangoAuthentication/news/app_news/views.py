from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

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


class NewsDetailView(FormMixin, DetailView):
    template_name = 'news/news_detail.html'
    model = News

    def post(self, request, news_pk):
        news = News.objects.get(pk=news_pk)
        if request.user.is_authenticated:
            form = CommentFormIsAuth(request.POST)
        else:
            form = CommentFormNotIsAuth(request.POST)

        if form.is_valid():
            # News.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/news/news_detail')

        return render(request, 'news/news_detail.html', )


class LoginView(LoginView):
    template_name = 'users/login.html'


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
