from django.shortcuts import render
from shop.models import Category, Product


def main_page(request):
    return render(request, 'base.html')


def products_categories(request):
    products_categories = Category.objects.all()
    return render(request, 'shop/products_categories.html', context={'categories': products_categories})
