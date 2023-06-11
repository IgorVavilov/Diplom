from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from shop.models import *


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')


def shoppingcart(request):
    cart = Cart(request)
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    random_products = Product.objects.order_by('?')[:3]
    return render(request, 'cart/shoppingcart.html', {'cart': cart, 'categories': categories, 'products': products, 'random_products': random_products})

