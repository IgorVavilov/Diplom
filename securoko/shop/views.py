from django.shortcuts import render, get_object_or_404
from .models import *
from users.models import *
from .forms import ContactForm
from django.views.generic import ListView, DetailView, CreateView, FormView
from .utils import *
from cart.forms import CartAddProductForm



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    random_products = Product.objects.order_by('?')[:2]
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {'category': category, 'categories': categories, 'products': products, 'random_products': random_products, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/products.html', context)


def productdetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    random_products = Product.objects.order_by('?')[:3]
    categories = Category.objects.all()
    articles = Article.objects.all()
    cart_product_form = CartAddProductForm()
    context = {'categories': categories, 'product': product, 'random_products': random_products,
               'articles': articles, 'cart_product_form': cart_product_form}

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


class ShowArticle(DataMixin, DetailView):
    model = Article
    template_name = 'shop/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['article']
        # # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title="F,hfdf")
        return dict(list(context.items()) + list(c_def.items()))


class CategoryArticle(ListView):
    model = Article
    template_name = "shop/index.html"
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Категрия - ' + str(context['articles'][0].cat)
        context['cat_selected'] = context['articles'][0].cat_id
        # context['menu'] = menu
        return context
        # c = Category.objects.get(slug=self.kwargs['cat_slug'])
        # c_def = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
        # return dict(list(context.items()) + list(c_def.items()))