from .models import *
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginate_products(request, products, results):
    page = request.GET.get("page", 1)
    # result = 9
    paginator = Paginator(products, results)
    products = paginator.get_page(page)

    left_index = int(page) - 4
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 5
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, products


def user_content(request):
    categories = Category.objects.all()
    random_categories = Category.objects.order_by()[:3]
    products = Product.objects.filter(available=True)
    articles = Article.objects.all()
    random_products = Product.objects.order_by('?')[:3]
    return categories, random_categories, products, articles, random_products


class DataMixin:
    # paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs

        # cats = Category.objects.annotate(Count('blog'))
        categories = Category.objects.all()

        # создание возможности отображения/неотображения пункта меню 'Добавить статью'
        # user_menu = menu.copy()
        # if not self.request.user.is_authenticated:
        #     user_menu.pop(0)

        # context['menu'] = user_menu
        context['categories'] = categories

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


def search_products(request, category_slug=None):
    search = ''

    if request.GET.get('keyword'):
        search = request.GET.get('keyword')

    category = None
    products = Product.objects.distinct().filter(Q(name__icontains=search) | Q(full_description__icontains=search))

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return products, category, search

