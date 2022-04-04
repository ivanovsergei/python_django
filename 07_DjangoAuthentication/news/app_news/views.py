from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponse
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

    def get_context_data(self, *args, **kwargs):
        """Добавляет дополнительную форму создания комментария в контекст."""
        context = super(NewsDetailView, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            comment_form = CommentFormIsAuth()
        else:
            comment_form = CommentFormNotIsAuth()
        context["comment_form"] = comment_form
        return context


class CommentFormView(View):

    def get(self, request):
        if request.user.is_authenticated:
            comment_form = CommentFormIsAuth(request.POST)
        else:
            comment_form = CommentFormNotIsAuth(request.POST)
        return render(request, 'comment/comment_add.html', context={'comment_form': comment_form})

    def post(self, request, news_pk, *args, **kwargs):
        if request.user.is_authenticated:
            comment_form = CommentFormIsAuth(request.POST)
            is_auth = True
        else:
            comment_form = CommentFormNotIsAuth(request.POST)
            is_auth = False

        if comment_form.is_valid():
            data = comment_form.cleaned_data
            data["news_id"] = news_pk
            if is_auth:
                data["user_name"] = User.objects.get(pk=self.request.user.id)
            else:
                data["user_name"] = User.objects.get(pk=2)
            Comment.objects.create(**data)
            return HttpResponseRedirect(f'/news/{news_pk}')

        return render(request, 'comment/comment_add.html', context={'comment_form': comment_form})


class LoginView(LoginView):
    template_name = 'users/login.html'


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
