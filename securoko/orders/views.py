from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import *


def order_create(request):
    cart = Cart(request)
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    random_products = Product.objects.order_by('?')[:3]
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # Очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order, 'categories': categories, 'products': products, 'random_products': random_products})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/checkout.html', {'cart': cart, 'form': form, 'categories': categories, 'products': products, 'random_products': random_products})
