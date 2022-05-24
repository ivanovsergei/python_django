from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import MainBlogListView, BlogDetailView, BlogEditFormView, img_upload, blog_upload

urlpatterns = [
    path('', MainBlogListView.as_view(), name='main'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:element_id>/edit', BlogEditFormView.as_view()),
    path('blog_upload/', blog_upload, name='blog_upload'),
    path('img_upload/', img_upload, name='img_upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
