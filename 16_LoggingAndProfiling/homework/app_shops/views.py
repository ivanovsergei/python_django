from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import Good, Account
from .forms import BalanceForm
from app_cart.forms import CartAddGoodForm
from datetime import datetime, timedelta
from django.utils import timezone
import logging
from django.contrib.auth.models import User


logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler()
c_handler.setLevel(logging.INFO)
c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
logger.addHandler(c_handler)


class MainShopListView(ListView):
    model = Good
    template_name = 'shop/main.html'
    context_object_name = 'goods'

    def get_queryset(self):
        queryset = Good.objects.prefetch_related('shops').all()
        return queryset


def account(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    logger.info('Запрошена страница аккаунта')
    user_id = request.user.id
    try:
        user = Account.objects.get(user_id=user_id)
    except ObjectDoesNotExist:
        user = Account.objects.create(user_id=user_id)
    balance = user.balance

    if 100 < user.spend_money < 200:
        user.status = 'a'
        user.save(update_fields=['status'])
    else:
        user.status = 'h'
        user.save(update_fields=['status'])
    status = user.get_status_display()
    return render(request, 'account/account.html', context={
        'balance': balance,
        'status': status,
    })


class AccountRefillView(View):

    def get(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied()
        balance_form = BalanceForm()
        return render(request, 'account/account_refill.html', context={'balance_form': balance_form})

    def post(self, request):
        balance_form = BalanceForm(request.POST)
        user_id = request.user.id

        if balance_form.is_valid():
            user = Account.objects.get(user=user_id)
            user.balance = balance_form.cleaned_data['balance']
            user.save(update_fields=['balance'])
            return HttpResponseRedirect('/account/account_refill')

        return render(request, 'account/account_refill.html', context={'balance_form': balance_form})


def good_detail(request, id):
    good = get_object_or_404(Good, id=id,)
    cart_good_form = CartAddGoodForm()
    return render(request, 'good/detail.html', {'good': good,
                                                'cart_good_form': cart_good_form})


def good_filter(request, pk):
    goods = Good.objects.all()
    if pk == 1:
        week = datetime.now(tz=timezone.utc) - timedelta(minutes=7*24*60)
        goods = goods.filter(created__gte=week)
    elif pk == 2:
        month = datetime.now(tz=timezone.utc) - timedelta(minutes=30*24*60)
        goods = goods.filter(created__gte=month)
    elif pk == 3:
        goods = goods
    return render(request, 'good/filter.html', {'goods': goods})
