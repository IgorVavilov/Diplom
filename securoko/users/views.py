from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from shop.utils import user_content

from .forms import CustomUserCreationForm, ProfileForm
from shop.models import Category, Product
from .forms import ContactForm


def profiles(request):
    prof = Profile.objects.all()
    context = {'profiles': prof}
    return render(request, 'users/index.html', context)


def login_user(request):
    categories, random_categories, products, articles, random_products = user_content(request)
    if request.user.is_authenticated:
        return redirect('profile_form')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, 'Пользователь не существует')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Пользователь либо пароль не верны')
    context = {'categories': categories,
               'random_products': random_products,
               'articles': articles,}
    return render(request, 'users/login_register.html', context)


def logout_user(request):
    logout(request)
    messages.info(request, "Пользователь успешно вышел!")
    return redirect('login')


def register_user(request):
    categories, random_categories, products, articles, random_products = user_content(request)
    page = 'register'
    form = CustomUserCreationForm()
    context = {'page': page,
               'form': form,
               'categories': categories,
               'random_products': random_products,
               'articles': articles,}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = new_user.username.lower()
            new_user.save()
            profile = Profile.objects.create(
                user=new_user,
                username=new_user.username,
                email=new_user.email,
                first_name=new_user.first_name,
                last_name=new_user.last_name,
                phone_number=new_user.phone_number,
            )

            messages.success(request, 'Учетная запись успешна создана')
            login(request, new_user)
            return render(request, 'users/register_done.html', context)
        else:
            messages.error(request, 'Произошла ошибка во время регистрации')
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def user_account(request):
    categories, random_categories, products, articles, random_products = user_content(request)
    prof = request.user.profile
    context = {'profile': prof,
               'categories': categories,
               'random_products': random_products,
               'articles': articles,}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def edit_account(request):
    categories, random_categories, products, articles, random_products = user_content(request)
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('account')

    context = {'form': form,
               'categories': categories,
               'random_products': random_products,
               'articles': articles,}
    return render(request, 'users/profile_form.html', context)


def contact(request):
    categories, random_categories, products, articles, random_products = user_content(request)
    recipient = Profile.objects.get(username="admin")
    form = ContactForm()
    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            print('message.sender:', message.sender)
            message.recipient = recipient

            # if sender:
            #     print('privet')
            #     message.name = sender
            #     print('message.name:', message.sender)
            #     message.sender_email = sender.email
            message.save()

            messages.success(request, 'Сообщение отправлено успешно')
            return redirect('contact')

    context = {'recipient': recipient,
               'form': form,
               'products': products,
               'categories': categories,
               'random_products': random_products,
               'articles': articles,}
    return render(request, 'users/contact.html', context)


@login_required(login_url='login')
def inbox(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    random_products = Product.objects.order_by('?')[:2]
    profile = request.user.profile
    message_request = profile.messages.all()
    unread_count = message_request.filter(is_read=False).count()
    context = {'categories': categories, 'products': products, 'message_request': message_request,
               'unread_count': unread_count}
    return render(request, 'users/inbox.html', context)


@login_required(login_url='login')
def view_message(request, pk):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    random_products = Product.objects.order_by('?')[:2]
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read is False:
        message.is_read = True
        message.save()
    context = {'categories': categories, 'products': products, 'message': message}
    return render(request, 'users/message.html', context)
