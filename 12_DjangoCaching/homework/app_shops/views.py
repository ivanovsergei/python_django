from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.shortcuts import render
from .models import Shop, Promotion, Balance, PaymentHistory, Offers
from django.core.cache import cache
from django.views.generic import ListView


class MainShopListView(ListView):
    model = Shop
    template_name = 'main.html'
    queryset = Shop.objects.all()


def account(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    user_id = request.user.id
    username = request.user.username
    try:
        balance = Balance.objects.get(user=user_id)
    except ObjectDoesNotExist:
        balance = Balance.objects.create(user_id=user_id, amount=0)

    promotion_list = Promotion.objects.filter(user=user_id)
    cache.set('promotion_list', promotion_list)
    offers = Offers.objects.filter(user=user_id)
    cache.set('offers', offers)

    payment_history = PaymentHistory.objects.filter(user=user_id)
    return render(request, 'account.html', context={
        'balance': balance,
        'promotions': promotion_list,
        'offers': offers,
        'payment_history': payment_history,
    })

