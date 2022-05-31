from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import Shop, Promotion
from django.core.cache import cache


def page_with_cached_fragment(request):
    shops = Shop.objects.all()
    return render(request, 'page_with_cached_fragment.html', context={
        'shops': shops
    })


def user_account(request):
    username = request.user.username
    balance = get_balance()

    promotion_cache_key = 'promotion: {}'.format(username)
    # if promotion_cache_key not in cache:
    #     promotions = get_promotions()
    #     cache.set(promotion_cache_key, promotions, 30*60)
    promotions = get_promotions()
    cache.get_or_set(promotion_cache_key, promotions, 30*60)

    offers_cache_key = 'offers:{}'.format(username)
    offers = get_offers()

    user_account_cache_data = {
        promotion_cache_key: promotions,
        offers_cache_key: offers
    }
    cache.set_many(user_account_cache_data)
    payment_history = get_payment_history()

    return render(request, 'users/account.html', context={
        'balance': balance,
        'promotions': promotions,
        'offers': offers,
        'payment_history': payment_history,
    })


def promotions(request):
    user_id = request.user.id
    promotion_list = Promotion.objects.filter(user=user_id)
    return render(request, 'account.html', context={'promotion_list': promotion_list})


class Login(LoginView):
    template_name = 'users/login.html'
