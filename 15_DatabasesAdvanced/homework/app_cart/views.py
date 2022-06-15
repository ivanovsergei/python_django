from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from app_shops.models import Good
from .cart import Cart
from .forms import CartAddGoodForm


@require_POST
def cart_add(request, good_id):
    cart = Cart(request)
    good = get_object_or_404(Good, id=good_id)
    form = CartAddGoodForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(good=good,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, good_id):
    cart = Cart(request)
    good = get_object_or_404(Good, id=good_id)
    cart.remove(good)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})