from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Blog, File
from .forms import BlogForm, MultiFileForm


class MainBlogListView(ListView):
    model = Blog
    template_name = 'main.html'
    queryset = Blog.objects.all()


class BlogDetailView(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog


class BlogEditFormView(View):

    def get(self, request, element_id):
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


def files_upload(request):
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
    return render(request, 'media/file_form_upload.html', {'form': form})
