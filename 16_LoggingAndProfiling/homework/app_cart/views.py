from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.db import IntegrityError
from app_shops.models import Good, Account
from .cart import Cart
from .forms import CartAddGoodForm


@require_POST
def cart_add(request, id):
    cart = Cart(request)
    good = get_object_or_404(Good, id=id)
    form = CartAddGoodForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(good=good,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, id):
    cart = Cart(request)
    good = get_object_or_404(Good, id=id)
    cart.remove(good)
    return redirect('cart:cart_detail')


def cart_purchase(request, id):
    cart = Cart(request)
    user_id = request.user.id
    cart_good = get_object_or_404(Good, id=id)
    good = Good.objects.get(id=id)
    user = Account.objects.get(user=user_id)
    try:
        for item in cart:
            if item['good'] == cart_good:
                cart_good_quantity = item['quantity']
                cart_good_price = item['price']
                good.stock -= cart_good_quantity
                good.top_sell += 1
                user.balance -= cart_good_price
                user.spend_money += cart_good_price
        good.save(update_fields=['stock', 'top_sell'])
        user.save(update_fields=['balance', 'spend_money'])
    except IntegrityError:
        pass
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
