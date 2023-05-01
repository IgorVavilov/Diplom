from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('product_list/<str:category_slug>', views.product_list, name='product_list'),
    # path(r'^(?P<category_slug>[-\w]+)/$',
    #     views.product_list,
    #     name='product_list_by_category'),
    path('productdetail/<str:id>/<str:slug>', views.productdetail, name='productdetail'),
]
