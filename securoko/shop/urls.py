from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('product_list', views.product_list, name='product_list_all'),
    path('product_list/<str:category_slug>', views.product_list, name='product_list'),
    path('productdetail/<str:id>/<str:slug>', views.productdetail, name='productdetail'),

    path('show_article/<str:slug>', views.show_article, name='article'),

    # path('article/<slug:article_slug>/', ShowArticle.as_view(), name='article'),
    # path('category_article/<slug:cat_slug>/', CategoryArticle.as_view(), name='category_article'),

]
