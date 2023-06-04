from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, FormView
from .forms import CustomUserCreationForm, ProfileForm
from shop.models import Category, Product


def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


# def user_profile(request, pk):
#     # prof = Profile.objects.get(id=pk)
#     prof = Profile.objects.get(id=pk)
#
#     # top_skill = prof.skill_set.exclude(description__exact="")
#     # other_skill = prof.skill_set.filter(description="")
#
#     context = {'profile': prof,}
#     return render(request, 'users/profile_form.html', context)


def login_user(request):
    categories = Category.objects.all()
    if request.user.is_authenticated:
        return redirect('profile_form')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password is incorrect')
    context = {'categories': categories}
    return render(request, 'users/login_register.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('login')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()
    categories = Category.objects.all()
    context = {'page': page, 'form': form, 'categories': categories}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = new_user.username.lower()
            new_user.save()
            profile = Profile.objects.create(user=new_user)

            messages.success(request, 'User account was created!')
            login(request, new_user)
            return render(request, 'users/register_done.html', context)
        else:
            messages.error(request, 'An error has occurred during registration')
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def user_account(request):
    prof = request.user.profile
    categories = Category.objects.all()
    random_products = Product.objects.order_by('?')[:1]
    context = {
        'profile': prof,
        'categories': categories,
        'random_products': random_products
    }
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    profile = request.user.profile # Необходима для отображения информации в форме, которые уже были созданы
    form = ProfileForm(instance=profile) # передаем данные профиля в форму
    categories = Category.objects.all()
    random_products = Product.objects.order_by('?')[:1]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form, 'categories': categories, 'random_products': random_products}
    return render(request, 'users/profile_form.html', context)


class ShowArticle(DetailView):
    model = Article
    template_name = 'users/article.html'
    slug_url_kwarg = 'article_slug'
    context_object_name = 'article'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['article']
        # context['menu'] = menu
        return context
        # c_def = self.get_user_context(title=context['article'])
        # return dict(list(context.items()) + list(c_def.items()))


class CategoryArticle(ListView):
    model = Article
    template_name = "shop/index.html"
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категрия - ' + str(context['articles'][0].cat)
        context['cat_selected'] = context['articles'][0].cat_id
        # context['menu'] = menu
        return context
        # c = Category.objects.get(slug=self.kwargs['cat_slug'])
        # c_def = self.get_user_context(title='Категория - ' + str(c.name), cat_selected=c.pk)
        # return dict(list(context.items()) + list(c_def.items()))