from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Article
from users.models import *

from .utils import search_products, paginate_products, user_content
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    categories, random_categories, products, articles, random_products = user_content(request)
    pr, cat, search = search_products(request, category_slug=category_slug)
    custom_range, pr = paginate_products(request, pr, 9)

    cart_product_form = CartAddProductForm()

    context = {'category': cat,
               'categories': categories,
               'products': pr,
               'random_products': random_products,
               'cart_product_form': cart_product_form,
               'search': search,
               'custom_range': custom_range,
               'articles': articles}
    return render(request, 'shop/product/products.html', context)


def productdetail(request, id, slug):
    categories, random_categories, products, articles, random_products = user_content(request)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {'categories': categories,
               'product': product,
               'random_products': random_products,
               'articles': articles,
               'cart_product_form': cart_product_form}

    return render(request, 'shop/product/productdetail.html', context)


def index(request):
    categories, random_categories, products, articles, random_products = user_content(request)
    cart_product_form = CartAddProductForm()
    context = {'categories': categories,
               'products': products,
               'random_categories': random_categories,
               'cart_product_form': cart_product_form,
               'articles': articles}
    return render(request, 'shop/index.html', context)


def show_article(request, slug):
    categories, random_categories, products, articles, random_products = user_content(request)
    article = get_object_or_404(Article, slug=slug)
    context = {'categories': categories,
               'products': products,
               'article': article,
               'random_products': random_products,
               'articles': articles}
    return render(request, 'shop/article.html', context)

