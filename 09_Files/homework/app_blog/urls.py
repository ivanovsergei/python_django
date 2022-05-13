from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import MainBlogListView, BlogDetailView, BlogEditFormView, files_upload

urlpatterns = [
    path('', MainBlogListView.as_view(), name='main'),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:element_id>/edit', BlogEditFormView.as_view()),
    path('files_upload/', files_upload, name='files_upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
