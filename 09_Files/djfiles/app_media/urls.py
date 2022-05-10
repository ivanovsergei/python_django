from django.conf.urls.static import static
from django.urls import path
from .views import ex_upload_file, items_list, update_price, model_form_upload, multi_file_upload
from django.conf import settings

urlpatterns = [
    path('exupload_file/', ex_upload_file, name='upload_file'),
    path('items/', items_list, name='items_list'),
    path('update_price/', update_price, name='update_price'),
    path('form_upload/', model_form_upload, name='form_upload'),
    path('multi_upload/', multi_file_upload, name='multi_upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
