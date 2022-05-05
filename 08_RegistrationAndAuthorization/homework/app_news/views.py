from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import News, Comment
from app_users.models import Profile
from .forms import NewsForm, CommentFormIsAuth, CommentFormNotIsAuth
from django.core.exceptions import PermissionDenied


class MainNewsListView(ListView):
    model = News
    template_name = 'main.html'
    queryset = News.objects.all()


class SearchResultsView(ListView):
    model = News
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = News.objects.filter(tags__istartswith=query)
        return object_list


class NewsFormView(View):

    def get(self, request):
        if not request.user.has_perm('app_news.add_news'):
            raise PermissionDenied()
        news_form = NewsForm()
        return render(request, 'news/news_add.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            News.objects.create(**news_form.cleaned_data)
            return HttpResponseRedirect('/news/news_add')
        return render(request, 'news/news_add.html', context={'news_form': news_form})


class NewsDetailView(DetailView):
    template_name = 'news/news_detail.html'
    model = News

    def get_context_data(self, *args, **kwargs):
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
                data["user_name"] = Profile.objects.get(pk=self.request.user.id)
            else:
                data["user_name"] = Profile.objects.get(pk=2)
            Comment.objects.create(**data)
            return HttpResponseRedirect(f'/news/{news_pk}')

        return render(request, 'comment/comment_add.html', context={'comment_form': comment_form})
