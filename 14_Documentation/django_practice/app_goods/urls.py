from django.urls import path
from .views import items_list, GoodList, GoodListMixin, GoodDetail

urlpatterns = [
    path('items/', items_list, name='items_list'),
    path('goods/', GoodList.as_view(), name='goods_list'),
    path('goods_mixin/', GoodListMixin.as_view(), name='goods_mixin'),
    path('goods_detail/<int:pk>', GoodDetail.as_view(), name='goods_detail'),

]
