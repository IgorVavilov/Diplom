from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import random


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'shop/product/products.html', context)


def productdetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    categories = Category.objects.all()
    context = {'categories': categories, 'product': product}
    return render(request, 'shop/product/productdetail.html', context)


def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {'categories': categories, 'products': products}
    return render(request, 'shop/index.html', context)


def contact(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'shop/contact.html', context)
