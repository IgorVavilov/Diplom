from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product_list', views.product_list, name='product_list_all'),
    path('product_list/<str:category_slug>', views.product_list, name='product_list'),
    path('productdetail/<str:id>/<str:slug>', views.productdetail, name='productdetail'),
    path('contact', views.contact, name='contact'),
]
