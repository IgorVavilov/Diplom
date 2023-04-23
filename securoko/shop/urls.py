from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.product_list, name='product_list'),
    path('product_list/<str:category_slug>', views.product_list, name='product_list_by_category'),
    path('product_list/<str:id>/<str:slug>', views.product_detail, name='product_detail'),
]
