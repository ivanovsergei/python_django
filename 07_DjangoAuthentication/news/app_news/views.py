from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from .forms import NewsForm, CommentAuthForm, CommentNotAuthForm
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

    if User.is_authenticated:
        form_class = CommentAuthForm

        def get_success_url(self):
            return reverse('news_detail', kwargs={'pk': self.object.id})

        def get_context_data(self, **kwargs):
            context = super(NewsDetailView, self).get_context_data(**kwargs)
            context['form'] = CommentAuthForm(initial={'post': self.object})
            return context
    else:
        form_class = CommentNotAuthForm

        def get_success_url(self):
            return reverse('news_detail', kwargs={'pk': self.object.id})

        def get_context_data(self, **kwargs):
            context = super(NewsDetailView, self).get_context_data(**kwargs)
            context['form'] = CommentNotAuthForm(initial={'post': self.object})
            return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        print('Сохранение формы выключено.')
        # form.save()
        return super(NewsDetailView, self).form_valid(form)


class LoginView(LoginView):
    template_name = 'users/login.html'


class LogoutView(LogoutView):
    template_name = 'users/logout.html'
