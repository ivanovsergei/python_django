from django.urls import path
from .views import items_list, GoodList, GoodListMixin

urlpatterns = [
    path('items/', items_list, name='items_list'),
    path('goods/', GoodList.as_view(), name='good_list'),
    path('goods_mixin/', GoodListMixin.as_view(), name='good_mixin'),

]
