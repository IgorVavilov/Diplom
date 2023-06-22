from django.shortcuts import render, get_object_or_404
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import *
from django.contrib.auth import logout, login, authenticate
from users.models import Profile


def order_create(request):
    cart = Cart(request)
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    random_products = Product.objects.order_by('?')[:3]
    if request.user.is_authenticated:
        profile = request.user.profile

        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.owner = profile
                form.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                # Очистка корзины
                cart.clear()
                context = {'order': order,
                            'categories': categories,
                            'products': products,
                            'random_products': random_products}
                return render(request, 'orders/order/created.html', context)
        else:
            form = OrderCreateForm(instance=profile)
    elif request.method == 'POST':
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
            context = {'order': order,
                       'categories': categories,
                       'products': products,
                       'random_products': random_products}
            return render(request, 'orders/order/created.html', context)
    else:
        form = OrderCreateForm
    context = {'cart': cart,
               'form': form,
               'categories': categories,
               'products': products,
               'random_products': random_products}
    return render(request, 'orders/order/checkout.html', context)


def profile_orders(request, pk):
    orders = Order.objects.filter(owner=request.user.profile).order_by('id')
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    random_products = Product.objects.order_by('?')[:2]
    context = {'orders': orders,
               'categories': categories,
               'products': products,
               'random_products': random_products}
    return render(request, 'orders/order/profile_orders.html', context)