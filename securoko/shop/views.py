from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .forms import ContactForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    random_products = Product.objects.order_by('?')[:2]
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products, 'random_products': random_products}
    return render(request, 'shop/product/products.html', context)


def productdetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    random_products = Product.objects.order_by('?')[:3]
    categories = Category.objects.all()
    context = {'categories': categories, 'product': product, 'random_products': random_products}
    return render(request, 'shop/product/productdetail.html', context)


def index(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {'categories': categories, 'products': products}
    return render(request, 'shop/index.html', context)


def contact(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    random_products = Product.objects.order_by('?')[:2]
    form = ContactForm()
    context = {'categories': categories, 'products': products, 'form': form, 'random_products': random_products}
    return render(request, 'shop/contact.html', context)


# def create_message(request):
#     form = ContactMessage()
#     return render(request, 'shop/contact.html', {'form': form})