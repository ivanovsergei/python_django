from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from app_news.forms import NewsForm
from app_news.models import News, Comment
from django.views import generic


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


