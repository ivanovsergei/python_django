from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Good, Account
from .forms import BalanceForm


class MainShopListView(ListView):
    model = Good
    template_name = 'main.html'
    context_object_name = 'goods'

    def get_queryset(self):
        queryset = Good.objects.prefetch_related('shops').all()
        return queryset


def account(request):
    if not request.user.is_authenticated:
        raise PermissionDenied()
    user_id = request.user.id
    user = Account.objects.get(user=user_id)
    try:
        balance = user.balance
    except ObjectDoesNotExist:
        balance = Account.objects.create(user=user_id, amount=0)

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
            print(balance_form.cleaned_data['balance'])
            return HttpResponseRedirect('/account/account_refill')

        return render(request, 'account/account_refill.html', context={'balance_form': balance_form})
