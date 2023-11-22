from django.contrib import admin
from shop.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    prepopulated_fields = {'slug': ('category_name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name',
                    'price', 'available']
    list_editable = ['price', 'available']
    list_filter = ['category', 'available']
    prepopulated_fields = {'slug': ('product_name',)}
