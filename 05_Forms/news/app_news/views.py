from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from app_news.forms import UserForm, NewsForm
from app_news.models import User, News, Comment
from django.views import generic


class UserFormView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'profiles/register.html', context={'user_form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            # совершаем какую-либо логику(сохраняем в базу данных
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/profiles/register')

        return render(request, 'profiles/register.html', context={'user_form': user_form})


class UserEditFormView(View):
    def get(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = UserForm(instance=user)
        return render(request, 'profiles/edit.html', context={'user_form': user_form,
                                                              'profile_id': profile_id})

    def post(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = UserForm(request.POST, instance=user)
        if user_form.is_valid():
            user.save()
        return render(request, 'profiles/edit.html', context={'user_form': user_form,
                                                              'profile_id': profile_id})


class NewsListView(generic.ListView):
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


class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'


