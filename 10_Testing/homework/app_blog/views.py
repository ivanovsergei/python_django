from _csv import reader

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Blog, File
from .forms import BlogForm, MultiFileForm, UploadPriceForm


class MainBlogListView(ListView):
    model = Blog
    template_name = 'main.html'
    queryset = Blog.objects.all()


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog

    def get_context_data(self, *args, **kwargs):
        context = super(BlogDetailView, self).get_context_data(*args, **kwargs)
        blog_id = (self.request.META['PATH_INFO'])
        for elem in blog_id:
            if elem.isdigit():
                pk = elem
                object_list = File.objects.filter(blog__id=pk)
            else:
                object_list = False

            context["article_files"] = object_list
        return context


class BlogEditFormView(View):

    def get(self, request, element_id):
        if not request.user.is_authenticated:
            raise PermissionDenied()
        blog = Blog.objects.get(id=element_id)
        blog_form = BlogForm(instance=blog)
        return render(request, 'blog/blog_edit.html', context={'blog_form': blog_form,
                                                               'element_id': element_id})

    def post(self, request, element_id):
        blog = Blog.objects.get(id=element_id)
        blog_form = BlogForm(request.POST, instance=blog)
        if blog_form.is_valid():
            blog.save()
        return render(request, 'blog/blog_edit.html', context={'blog_form': blog_form,
                                                               'element_id': element_id})


def img_upload(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    elif request.method == 'POST':
        form = MultiFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('file_field')
            for f in files:
                instance = File(file=f)
                instance.save()
            return redirect('/')
    else:
        form = MultiFileForm()
    return render(request, 'media/img_form_upload.html', {'form': form})


def blog_upload(request):
    if request.method == 'POST':
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            upload_file = upload_file_form.cleaned_data['file'].read()
            file_str = upload_file.decode('utf-8').split()
            csv_reader = reader(file_str, delimiter=":")
            for row in csv_reader:
                print(row[0])
                Blog.objects.create(article=row[0], created_at=row[1])
            return HttpResponse(content='Статьи были успешно добавлены', status=200)
    else:
        upload_file_form = UploadPriceForm()

    return render(request, 'media/upload_file.html', {'form': upload_file_form})
