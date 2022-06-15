from django.conf.urls import url
from . import views


urlpatterns = [
    url('<int:good_id>', views.cart_detail, name='cart_detail'),
    url('add/<int:good_id>', views.cart_add, name='cart_add'),
    url('remove/<int:good_id>', views.cart_remove, name='cart_remove'),
]
