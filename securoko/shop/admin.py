from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_field = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'manufacturer', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['manufacturer', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_field = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
